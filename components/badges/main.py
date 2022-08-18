import streamlit as st
from htbuilder import a, img

# [![GitHub stars](https://img.shields.io/github/stars/Naereen/StrapDown.js.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/Naereen/StrapDown.js/stargazers/)
_SUPPORTED_TYPES = ("pypi", "streamlit", "github")


def badge(type: str, name: str = None, url: str = None):
    """Easily create a badge!

    Args:
        type (str): Badge type. Can be "pypi" or "streamlit"
        name (str): Name of the PyPI package or GitHub repository. Mandatory when using type="pypi"
        url (str): URL of the Streamlit Cloud app. Mandatory when using type="streamlit"
    """

    assert type, "Type must be given!"

    assert type in _SUPPORTED_TYPES, (
        f"This type {type} is not supported! Supported types are"
        f" {_SUPPORTED_TYPES}"
    )

    badge_html = None

    if type == "pypi":
        assert name, "You must give a valid PyPI package name!"
        badge_html = str(
            a(href=f"https://pypi.org/project/{name}")(
                img(src=f"https://badge.fury.io/py/{name}.svg")
            )
        )

    if type == "streamlit":
        assert url, "You must provide a valid URL for the Streamlit app"
        badge_html = str(
            a(href=url)(
                img(
                    src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg"
                )
            )
        )

    if type == "github":
        assert name, (
            "You must give a valid GitHub repository name! Something like"
            " 'author/name'"
        )
        badge_html = str(
            a(href=f"https://github.com/{name}")(
                img(
                    src=f"https://img.shields.io/github/stars/{name}.svg?style=social&label=Star&maxAge=2592000"
                )
            )
        )

    if badge_html is not None:
        st.write(badge_html, unsafe_allow_html=True)


def example_pypi():
    badge(type="pypi", name="plost")
    badge(type="pypi", name="streamlit")


def example_streamlit():
    badge(type="streamlit", url="https://plost.streamlitapp.com")


def example_github():
    badge(type="github", name="streamlit/streamlit")
