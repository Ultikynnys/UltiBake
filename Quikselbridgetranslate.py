import bpy
import os

# Define a function to process the images
def process_images(folder_path):
    # Create a new folder for the modified images
    output_folder = os.path.join(folder_path, "modified_images")
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each EXR image in the selected folder and its subfolders
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(".exr"):
                image_path = os.path.join(root, filename)
                bpy.ops.image.open(filepath=image_path)
                image = bpy.data.images.load(image_path)

                # Determine the channel to use based on the filename suffix
                if "MR" in filename:
                    channel_index = 0  # Red channel
                elif "DpRA" in filename:
                    channel_index = 2  # Blue channel
                else:
                    continue  # Ignore the image if it doesn't have the specified suffix

                # Replace all channels with the selected channel
                pixels = list(image.pixels)
                for i in range(0, len(pixels), 4):
                    selected_value = pixels[i + channel_index]
                    pixels[i] = selected_value  # Red channel
                    pixels[i + 1] = selected_value  # Green channel
                    pixels[i + 2] = selected_value  # Blue channel
                    pixels[i + 3] = selected_value  # Alpha channel

                image.pixels = pixels

                output_filename = os.path.splitext(filename)[0] + ".png"
                output_path = os.path.join(output_folder, output_filename)
                image.filepath_raw = output_path
                image.file_format = 'PNG'
                image.save()

    print("Modified images saved to:", output_folder)

# Define a function to be called after directory selection
def process_selected_directory(self, context):
    folder_path = self.directory

    # Process the images with the determined channel
    process_images(folder_path)

# Create an operator to invoke the directory browser
class SimpleOperator(bpy.types.Operator):
    bl_idname = "wm.select_directory"
    bl_label = "Select Directory"

    directory: bpy.props.StringProperty(subtype="DIR_PATH")

    def execute(self, context):
        process_selected_directory(self, context)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

# Register the operator
bpy.utils.register_class(SimpleOperator)

# Invoke the operator to select a directory
bpy.ops.wm.select_directory('INVOKE_DEFAULT')
