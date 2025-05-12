import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv




def sim_plot(grid, sim_time):
    
    # Method and slider to update all visuals based on the time selection
    def update_time(time):
        k = np.count_nonzero(t < time)
        p.add_mesh(grid.car.translate((h[k], 0, 0)), name='ego', render=False)
        p.update()

    # Data to display
    t = np.arange(0, sim_time, 0.04)
    h = np.zeros(np.size(t))


    # Define plotter

    p = pv.Plotter()
    p.add_mesh(grid.car, name='ego', render=False)
    p.show(auto_close=False, interactive=True, interactive_update=True)



    time_slider = p.add_slider_widget(
        update_time,
        [np.min(t), np.max(t)],
        0,
        'Time',
        (0.25, 0.9),
        (0.75, 0.9),
        interaction_event='always',
    )

    # Start incrementing time automatically
    for i in range(1, len(t)):
        h[i] = np.sin(t[i])
        time_slider.GetSliderRepresentation().SetValue(t[i])
        update_time(t[i])

    p.show()  # Keep plotter open to let user play with time slider

if __name__ == "__main__":
    sim_plot()