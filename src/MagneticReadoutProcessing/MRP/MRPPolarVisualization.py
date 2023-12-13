"""  plotting function to render polar plots of a reading """

import matplotlib.pyplot as plt
from matplotlib import cm, colormaps
import math
import numpy as np
# CUSTOM CLASSES

from MRP import MRPReading, MRPHelpers


class MRPPolarVisualization():
    """ Provides simple functions to plot a MRPReading using matplotlib in 2d or 3d"""

    measurement = None
    theta = None
    phi = None
    n_theta = int()
    n_phi = int()
    sensor_distance_radius = int()
    sensor_id = int()
    theta_radians = 0.5 * math.pi # 90 degree half phere
    phi_radians = 2 * math.pi # 360 degree
    title = ""
    def __init__(self, _reading: MRPReading.MRPReading):
        """
        Creates a MRPVisualization instance to plot a given reading in 2D/3D

        :param _reading: MRPReading instance of the reading to visualize
        :type _reading: MRPReading

        """
        self.measurement: MRPReading.MRPReading = _reading # REFERENCE!

        self.n_theta: int = self.measurement.measurement_config.n_theta
        self.n_phi: int = self.measurement.measurement_config.n_phi
        self.sensor_distance_radius: int = self.measurement.measurement_config.sensor_distance_radius
        self.sensor_id: int = self.measurement.measurement_config.sensor_id
        self.theta_radians: float = self.measurement.measurement_config.theta_radians
        self.phi_radians:float = self.measurement.measurement_config.phi_radians

        # CREATE A POLAR COORDINATE GRID
        self.theta, self.phi = np.mgrid[0.0:self.theta_radians:self.n_theta * 1j, 0.0:self.phi_radians:self.n_phi * 1j]

        # CALCULATE X Y Z GRID FOR PLOTTING
        self.x = self.sensor_distance_radius * np.sin(self.theta) * np.cos(self.phi)
        self.y = self.sensor_distance_radius * np.sin(self.theta) * np.sin(self.phi)
        self.z = self.sensor_distance_radius * np.cos(self.theta)

        # set default title
        self.set_title("")

    def set_title(self, _title: str):
        if not _title or len(_title) <= 0:
            _title = "PolarVisualisation of {}".format(self.measurement.get_name())
        self.title = _title
    def create_plot(self):
        inp = []
        # NORMALIZE DATA
        normalisation_factor = 1.0
        min_val = float('inf')
        max_val = -float('inf')
        center_val =(max_val-min_val)
        # GET MIN MAX VALUE
        for r in self.measurement.data:
            value = r.value
            if value < min_val:
                min_val = value - 0.1
            if value > max_val:
                max_val = value + 0.1

        # INSERT EXISTING DATA
        # AND ADD MISSING DATAPOINTS
        # NORMALIZE THEM
        #color_value_normalizer = cm.colors.CenteredNorm(halfrange=0.0, vcenter=0.0, clip=True)
        color_value_normalizer = cm.colors.Normalize( vmin=-1, vmax=1)
        for j in self.phi[0, :]:
            for i in self.theta[:, 0]:
                added = False
                # CHECK IF DATA EXSITS
                for r in self.measurement.data:
                    dj = r.phi
                    di = r.theta

                    if j == dj and i == di:
                        value = r.value
                        # BETWEEN -1 and 1 (maybe used in the feature)
                        normalized_value = MRPHelpers.translate(value, min_val, max_val, -1.0, 1.0)
                        # FOR PLOTTING BETWEEN 0 - 1
                        color_normalized_value = color_value_normalizer(normalized_value)
                        inp.append([j, i, color_normalized_value])
                        added = True
                        break
                if not added:
                   inp.append([j, i, 0.0])


        inp = np.array(inp)
        # reshape the input array to the shape of the x,y,z arrays.
        reshaped_reading_results = inp[:, 2].reshape((self.n_phi, self.n_theta)).T
        # Set colours and render
        fig = plt.figure(figsize=(10, 8)) # *100pixel

        ax = fig.add_subplot(111, projection='3d')
        ax.set_title('{} - Temperature-Error'.format(self.title))
        # COLORMAP
        ## coolwarm -> blue = negative red = positive values
        cmap = cm.coolwarm(reshaped_reading_results)

        #ax.pcolormesh(self.x, self.y, self.z, vmin=-1., vmax=1., cmap=cmap)
        ax.plot_surface(self.x, self.y, self.z, rstride=1, cstride=1, facecolors=cmap, alpha=1, linewidth=1, shade=False,
                        antialiased=False)
        ax.set_aspect("equal")
        return ax, fig


    def plot2d_top(self, _filename: str = None):
        """
        Visualize the reading as 2D top-down plot

        :param _filename: If set to a valid filepath, the plot will be saved to a .png file
        :type _filename: MRPReading

        """
        lax, lfig = self.create_plot()
        # SAVE CURRENT VIEW
        lazim = lax.azim
        ldist = lax.dist
        lelev = lax.elev
        # SET NEW VALUES
        lax.azim = 0
        lax.dist = 6
        lax.elev = 90

        # SAVE FIGURE IF NEEDED
        if _filename is not None:
            lfig.savefig(_filename)
        else:
            lfig.show()

        # RESTORE VIEW
        lax.azim = lazim
        lax.dist = ldist
        lax.elev = lelev
        # CLOSE FIGURE
        plt.close(lfig)

    def plot2d_side(self, _filename: str = None):
        """
        Visualize the reading as 2D side view plot

        :param _filename: If set to a valid filepath, the plot will be saved to a .png file
        :type _filename: MRPReading

        """
        lax, lfig = self.create_plot()
        # SAVE CURRENT VIEW
        lazim = lax.azim
        ldist = lax.dist
        lelev = lax.elev
        # SET NEW VALUES
        lax.azim = 0
        lax.dist = 6
        lax.elev = 0

        # SAVE FIGURE IF NEEDED
        if _filename is not None:
            lfig.savefig(_filename, dpi=1200)
        else:
            lfig.show()

        # RESTORE VIEW
        lax.azim = lazim
        lax.dist = ldist
        lax.elev = lelev
        # CLOSE FIGURE
        plt.close(lfig)

    def plot3d(self, _filename: str = None):
        """
        Visualize the reading as 3D plot

        :param _filename: If set to a valid filepath, the plot will be saved to a .png file
        :type _filename: MRPReading

        """
        lax, lfig = self.create_plot()

        if _filename is not None:
            lfig.savefig(_filename, dpi=1200)
        else:
            lfig.show()

        plt.close(lfig)

