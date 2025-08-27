  for metric in ["BSS", "CRPSS", "AUC", "ACC"]:
            metric_start = position_index

            for model in plot_order:
                try:
                    data = results[var][model][season][metric]
                    values = metric_keys[metric](data)

                    if values is None:
                        continue

                    if isinstance(values, xr.DataArray):
                        values = values.values.flatten()

                    box_data.append(values)
                    model_color = model_colors.get(model, "#999999")
                    box_colors.append(model_color)
                    positions.append(position_index)

                    # Save color info for legend
                    if model not in legend_handles:
                        legend_handles[model] = plt.Line2D([0], [0], color=model_color, marker='s',
                                                           linestyle='', markersize=10, label=model)

                    position_index += 1
                except Exception as e:
                    print(f"⚠️ Skipped {metric} for {model} {season} {var} due to: {e}")
                    continue

            metric_center = (metric_start + position_index - 1) / 2
            xtick_positions.append(metric_center)
            xtick_labels.append(metric)
            vline_positions.append(position_index - 0.5)
            position_index += spacing

        if not box_data:
            continue
