import unittest
from unittest.mock import patch
import roop
from roop.core import parse_args, pre_check, limit_resources, start
from roop.utilities import create_temp, normalize_output_path, move_temp

import time

class YourScriptTest(unittest.TestCase):

    def setUp(self):
        parse_args()
        limit_resources()

        if not pre_check():
            raise SystemExit(1)

        # Initialize instance attributes
        self.paths_initialized = False
        self.app_running = False
        self.processing_started = False

    def test_image_processing(self):
        # Initialize paths
        data = {'source_path': 'source_image.jpg', 'target_path': 'target_image.jpg', 'output_path': 'output.jpg'}
        self.initialize_paths(data)

        # Create the application
        self.create_app()

        # Iterate 100 times through the image process
        for iteration in range(100000):
            # Update source and target paths for each iteration
            data['source_path'] = f'source_image_{iteration}.jpg'
            data['target_path'] = f'target_image_{iteration}.jpg'
            data['output_path'] = f'output_image_{iteration}.jpg'

            # Initialize paths with updated values
            self.initialize_paths(data)

            # Start processing with the updated paths
            self.start_processing(data)

            # Add assertions for expected behavior
            self.assertTrue(self.app_running, "App should be running")
            self.assertTrue(self.processing_started, "Processing should be started")

    def initialize_paths(self, data):
        # Debugging print statements
        print(f"DEBUG: source_path: {data['source_path']}")
        print(f"DEBUG: target_path: {data['target_path']}")
        print(f"DEBUG: output_path: {data['output_path']}")

        # Use updated paths for normalization
        normalized_output_path = normalize_output_path(
            data['source_path'], data['target_path'], data['output_path']
        )

        # More debugging print statements
        print(f"DEBUG: normalized_output_path: {normalized_output_path}")

        # Update the output_path in data
        data['output_path'] = normalized_output_path

        # Create a temporary directory for the updated output path
        create_temp(data['output_path'])
        self.paths_initialized = True

    def create_app(self):
        roop.globals.keep_frames = True
        roop.globals.keep_fps = True
        roop.globals.temp_frame_quality = 1
        roop.globals.output_video_quality = 1
        roop.globals.execution_provider = 'cuda'
        roop.globals.frame_processors = ['face_swapper', 'face_enhancer']
        self.app_running = True

    def start_processing(self, data):
        processed_file_path = start(source_path=data['source_path'], target_path=data['target_path'],output_path=data['output_path'])
        move_temp(data['target_path'], data['output_path'])
        self.processing_started = True

if __name__ == '__main__':
    unittest.main()
