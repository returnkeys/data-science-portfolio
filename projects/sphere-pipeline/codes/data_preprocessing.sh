# Function to get the first N actual level values from a file
get_model_levels() {
    local file=$1
    local n=$2
    cdo showlevel "$file" | tr ' ' '\n' | grep -E '^[0-9\.]+$' | head -n "$n" | paste -sd, -
}

# Loop over variables
for var in "${!variables[@]}"; do
    IFS=' ' read -r var_model var_obs unit detrend_needed <<< "${variables[$var]}"

    for model in "${models[@]}"; do
        echo "Processing model: $model, variable: $var"

        input_dir="/work/datasets/models/C3S_seasfc/${model}/${var}/"
        output_base_dir="/work/users/epourjavad/sphere/anomaly_calculation/models/C3S_seasfc/${model}/anomaly_seasmean/${var}/"
        mkdir -p "$output_base_dir"

        for start_date in "${!seasons[@]}"; do
            season="${seasons[$start_date]}"
            output_dir="${output_base_dir}${start_date}/"
            mkdir -p "$output_dir"

            for year in $years; do
                file="${input_dir}${var}_${year}${start_date}.nc"
                if [[ -f "$file" ]]; then
                    filename=$(basename "$file")
                    output_file="${output_dir}${filename%.nc}_monmean.nc"
                    season_file="${output_dir}${filename%.nc}_${season}.nc"

                    # Create unique temp file
                    temp_file="temp_${model}_${var}_${year}${start_date}.nc"
                    [ -f "$temp_file" ] && rm -f "$temp_file"

                    # Detect variable inside file
                    if cdo sinfon "$file" | grep -qE "${var_model}|${var_obs}|tp|t2m|d2m|strd|ssrd|sfcWind|u10"; then
                        if cdo sinfon "$file" | grep -q "$var_model"; then
                            var_name="$var_model"
                        elif cdo sinfon "$file" | grep -q "tp"; then
                            var_name="tp"
                        else
                            var_name="t2m"
                        fi