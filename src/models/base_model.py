# BaseModel - A generic LLM model
#
# This class represents a generic LLM model. All the subclasses must implement the get_answer method.
#
# Copyright (C) 2023 Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo sasadangelo@gmail.com
#
# SPDX-License-Identifier: MIT
class Model:
    def __init__(self, temperature, model_name, embeddings):
        super().__init__()
        self.model_name = model_name
        self.temperature = temperature
        self.embeddings = embeddings

    # Common logic for generating a response
    def get_answer(self, messages) -> tuple[str, float]:
        pass