# ChatBotApp - Manage Streamlit Application and Navigation
#
# This file defines the ChatBotApp class, which is responsible for managing the Streamlit chatbot. 
# It initializes the initial page, handles page selection, and serves as the entry point for running the 
# application.
#
# Copyright (C) 2023 Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo sasadangelo@gmail.com
#
# This file is part of the Running Data Analysis project.
#
# SPDX-License-Identifier: MIT
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from src.ui.chatbot_page import ChatBotPage

# Decorator to implement the Singleton design pattern.
# A singleton ensures that there is only one instance of a specific class
# and provides a global access point to this instance.
def singleton(cls):
    instances = {}

    # Function to get the singleton instance.
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

# This class is responsible for managing the Streamlit application
# and navigation between different pages. It initializes the initial page, handles page selection,
# and serves as the entry point for running the application.
@singleton
class ChatBotApp:
    # The constructor load all the activities in the gpx folder of the logged in user.
    def __init__(self):
        self.current_page = None

    # Runs the TrainingApp and initializes the first page as ActivityOverviewPage.
    def run(self):
        self.select_page(ChatBotPage())

    # Selects and renders the current page based on user navigation logic.
    def select_page(self, page):
        # Here you can add logic for navigating between different pages.
        # For example, if you want to show the ActivityOverviewPage as the initial page:
        self.current_page = page
        self.current_page.render()

if __name__ == "__main__":
    _ = load_dotenv(find_dotenv())
    app = ChatBotApp()
    app.run()