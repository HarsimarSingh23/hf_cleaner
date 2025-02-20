import time
from pathlib import Path
import streamlit as st
from hf_cleaner.utils.file_utils import hf_cache_loc, get_file_info, delete_item
from .BaseTemplate import BaseTemplate


class DashboardTemplate(BaseTemplate):
    def __init__(self):
        self.file_loc: str = hf_cache_loc()
        self.template_name = "Profile Dashboard Template"
        self.layout()

    def layout(self):
        st.write(f"**HF File Directory:** {self.file_loc}")

        # Get the list of models
        model_list = self._get_file_list(self.file_loc, is_list_models=True, is_list_datasets=False)

        # Create a dropdown to select a model
        model_names = [model.name for model in model_list]
        selected_model_name = st.selectbox("Select a Model", model_names)

        # Find the selected model's path
        selected_model_path = next(model for model in model_list if model.name == selected_model_name)

        # Display the selected model's name and metadata
        if selected_model_path:
            st.write(f"**Selected Model:** {selected_model_name}")
            metadata = self._get_model_metadata(selected_model_path)
            st.write("**Metadata:**")
            st.json(metadata)

    @staticmethod
    def _get_file_list(dir_path, is_list_models, is_list_datasets):
        items = list(Path(dir_path).glob('*'))
        model_list = []
        if is_list_models:
            model_list = [path for path in items if "models--" in path.name]
        if is_list_datasets:
            datasets_list = [path for path in items if "datasets--" in path.name]
            return model_list + datasets_list
        return model_list

    @staticmethod
    def _get_model_metadata(model_path):
        # Placeholder function to retrieve metadata
        # Replace this with actual logic to fetch metadata from the model path
        return {
            "model_name": model_path.name,
            "path": str(model_path),
            "last_modified": time.ctime(model_path.stat().st_mtime),
            "size": model_path.stat().st_size
        }


ds = DashboardTemplate()
ds.layout()