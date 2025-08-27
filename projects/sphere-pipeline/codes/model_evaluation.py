# Metric Calculations
def calculate_brier_score(forecast, observed):
    return ((observed - forecast) ** 2).mean(dim="time")

def categorize_data(data, dims="time"):
    q33 = data.quantile(0.33, dim=dims)
    q66 = data.quantile(0.66, dim=dims)
    below = data < q33
    normal = (data >= q33) & (data < q66)
    above = data >= q66
    return below, normal, above

def calculate_category_probabilities(forecast_data):
    below, normal, above = categorize_data(forecast_data, dims=("ensemble", "time"))
    return {
        "below": below.sum(dim="ensemble") / forecast_data.sizes["ensemble"],
        "normal": normal.sum(dim="ensemble") / forecast_data.sizes["ensemble"],
        "above": above.sum(dim="ensemble") / forecast_data.sizes["ensemble"]
    }

def calculate_bss(forecast_bs, reference_bs):
    return {cat: 1 - (forecast_bs[cat] / reference_bs[cat]) for cat in forecast_bs} | {
        "average": sum(1 - (forecast_bs[cat] / reference_bs[cat]) for cat in forecast_bs) / 3
    }

def process_crps(fcst, obs):
    return crps_for_ensemble(fcst, obs, ensemble_member_dim="ensemble", method="fair", reduce_dims=["time"])

def compute_auc_skill(forecast_data, obs_data):
    percentiles_fcst = forecast_data.quantile([0.33, 0.66], dim=('ensemble', 'time'))
    percentiles_obs = obs_data.quantile([0.33, 0.66], dim='time')

    below_mask = forecast_data < percentiles_fcst.sel(quantile=0.33)
    normal_mask = (forecast_data >= percentiles_fcst.sel(quantile=0.33)) & (forecast_data < percentiles_fcst.sel(quantile=0.66))
    above_mask = forecast_data >= percentiles_fcst.sel(quantile=0.66)

    below_prob = below_mask.sum(dim='ensemble') / forecast_data.sizes['ensemble']
    normal_prob = normal_mask.sum(dim='ensemble') / forecast_data.sizes['ensemble']
    above_prob = above_mask.sum(dim='ensemble') / forecast_data.sizes['ensemble']

    below_obs = (obs_data < percentiles_obs.sel(quantile=0.33)).astype(int)
    normal_obs = ((obs_data >= percentiles_obs.sel(quantile=0.33)) & (obs_data < percentiles_obs.sel(quantile=0.66))).astype(int)
    above_obs = (obs_data >= percentiles_obs.sel(quantile=0.66)).astype(int)

    auc_scores = {
        'below': roc_curve_data(below_prob, below_obs, thresholds=np.linspace(0, 1, 1000), reduce_dims=['time']).AUC,
        'normal': roc_curve_data(normal_prob, normal_obs, thresholds=np.linspace(0, 1, 1000), reduce_dims=['time']).AUC,
        'above': roc_curve_data(above_prob, above_obs, thresholds=np.linspace(0, 1, 1000), reduce_dims=['time']).AUC,
    }

    auc_skills = {k: 2 * auc_scores[k] - 1 for k in auc_scores}
    auc_skills['average'] = sum(auc_skills.values()) / 3
    return auc_skills
