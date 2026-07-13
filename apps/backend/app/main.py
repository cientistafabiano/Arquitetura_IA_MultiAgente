from core.state import SoberanaState
from app.graph import graph


def main():
    state = SoberanaState()
    result = graph.invoke(state)
    print(result)