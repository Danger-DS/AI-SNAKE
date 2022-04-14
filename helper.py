import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from IPython import display
font_thick = fm.FontProperties(fname = 'C:/Users/dange/OneDrive/Desktop/Portfolio/Snake-AI/Montserrat-SemiBold.otf', size = 20)
font = fm.FontProperties(fname = 'C:/Users/dange/OneDrive/Desktop/Portfolio/Snake-AI/Montserrat-Regular.otf', size = 13)

plt.ion()

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training Process', fontproperties = font_thick)
    plt.xlabel('Number of Games', fontproperties = font)
    plt.ylabel('Score', fontproperties = font)
    plt.plot(scores, label = "Scores", color = "#FF0000", linewidth = 2.5, marker = '.', markersize = 5)
    plt.plot(mean_scores, label = "Mean Scores", linewidth = 2.5, marker = '.', markersize = 5)
    plt.ylim(ymin = 0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(.1)
    plt.legend()