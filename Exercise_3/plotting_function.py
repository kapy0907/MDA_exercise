import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


def plot_temperature_4_models(data, vmin=-15.0, vmax=15.0,
                              cmap='coolwarm', projection=ccrs.Mercator(),
                              statistics=True, save='temperature.png'):
    """
    Plotting routine for comparison of four models.
    Parameters
    ----------
    data : dict
        keys = model name,
        values = 2D temperature in °C with dimensions lon, lat
    vmin, vmax (optional) : float
        limits for temperature range to make plots comparable
        default: vmin=-15.0, vmax=15.0
    cmap : colormap object or matplotlib colormap name
        colormap for plotting
    projection : cartopy projection
        Cartopy projection object containing all the projection information of
        the data
    statistics (optional): boolean
        print statistics
    statistics (optional): string
        path + filename where to save file
    Returns:
    --------
    None.

    """

    plt.close()
    fig, axes = plt.subplots(2, 2, subplot_kw={'projection': projection})
    [[ax1, ax2], [ax3, ax4]] = axes

    model_axes = [ax1, ax2, ax3, ax4]

    for model, model_ax in zip(data.keys(), model_axes):

        im = model_ax.pcolormesh(data[model].lon, data[model].lat,
                                 data[model], vmin=vmin, vmax=vmax,
                                 cmap='coolwarm',
                                 transform=ccrs.PlateCarree(),
                                 )
        model_ax.axes.coastlines()
        model_ax.set_title(model)

        if statistics:
            bias = str(data[model].mean().values.round(2))
            rmse = str(np.sqrt((data[model]**2).mean()).values.round(2))

            model_ax.text(0.027, 0.047,
                          'RMSE: ' + rmse + ' \nBIAS: ' + bias,
                          bbox=dict(facecolor='white', alpha=0.8),
                          transform=model_ax.transAxes,
                          )

    fig.subplots_adjust(bottom=0.1, top=0.95, left=0.1, right=0.8,
                        wspace=0.1, hspace=0.1)

    cb_ax = fig.add_axes([0.83, 0.11, 0.02, 0.83])
    cbar = fig.colorbar(im, cax=cb_ax)
    cbar.ax.set_ylabel(r'$\Delta$ T [°C]')

    plt.savefig(save, dpi=200)
    plt.show()
