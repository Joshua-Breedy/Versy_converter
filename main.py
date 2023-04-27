import flet as ft
from backend import *

def main(page: ft.Page):

    # page configuration
    page.title = "Versy"
    page.window_height = 600
    page.window_width = 600
    page.vertical_alignment = "center"

    # functions
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.visible = True
        selected_files.update()
        changeType(e)
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text(visible=False)
    progress = ft.Text(value="")
    page.overlay.append(pick_files_dialog)
    def convert(e):
        if findType(selected_files.value) in audioFileTypes:
            progress.value = "Converting audio file! Please wait..."
            page.update()
            convert_audio_file(selected_files.value, convertDropdown.value)
            progress.value = "Conversion complete"
        elif findType(selected_files.value) in videoFileTypes:
            progress.value = "Converting video file! Please wait..."
            page.update()
            convert_video_file(selected_files.value, convertDropdown.value)
            progress.value = "Conversion complete"
        elif findType(selected_files.value) in imageFileTypes:
            progress.value = "Converting image file! Please wait..."
            page.update()
            convert_image_file(selected_files.value, convertDropdown.value)
            progress.value = "Conversion complete"
        else:
            progress.value = "Unsupported file type"
        page.update()

    def changeType(e):
        print(findType(selected_files.value))
        if findType(selected_files.value) in audioFileTypes:
            convertDropdown.options = [
                ft.dropdown.Option("FLAC"),
                ft.dropdown.Option("MP3"), 
                ft.dropdown.Option("OGG"),
                ft.dropdown.Option("WAV")
            ]
        elif findType(selected_files.value) in videoFileTypes:
            convertDropdown.options = [
                ft.dropdown.Option("MP4"),
                ft.dropdown.Option("MKV"), 
                ft.dropdown.Option("AVI"),
                ft.dropdown.Option("MOV")
            ]
        elif findType(selected_files.value) in imageFileTypes:
            convertDropdown.options = [
                ft.dropdown.Option("PNG"),
                ft.dropdown.Option("JPG"), 
                ft.dropdown.Option("JPEG"),
                ft.dropdown.Option("GIF"),
                ft.dropdown.Option("BMP"),
                ft.dropdown.Option("TIFF")
            ]
        else:
            convertDropdown.options = [
                ft.dropdown.Option("Unsupported file type")
            ]
        page.update()

    # page elements
    introText = ft.Text("Welcome to Versy!", size=40, color="white", weight="bold")
    conversionText = ft.Text("Select below to begin file conversion", size=14, color="white", weight="bold")
    filePickButton = ft.ElevatedButton("Select file", icon=ft.icons.UPLOAD_FILE, on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=False))
    convertDropdown = ft.Dropdown(
        label="Select format", 
        border_color= "white",
        options=[
            ft.dropdown.Option("Select a file")
        ])
    convertDropdown.options
    convertButton = ft.ElevatedButton("Convert", icon=ft.icons.DOWNLOAD, on_click=convert)
    spacer = ft.Text("", size=5)

    # page layout
    introView = ft.Row(
        [
            ft.Column(
            [
                introText
                ],
                height=50
                )
                ],
        alignment=ft.MainAxisAlignment.CENTER
        )
    selectView = ft.Row(
        [
            ft.Column(
            [
                conversionText
                ]
                )
        ], 
        alignment=ft.MainAxisAlignment.CENTER
    )
    selectFileView = ft.Row(
        [
        ft.Column(
            [
                filePickButton, selected_files
                ]
            )
        ],
        alignment= ft.MainAxisAlignment.CENTER
    )
    filePickView = ft.Row(
        [
            ft.Column(
                [
                    convertDropdown
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    convertView = ft.Row(
        [
            ft.Column(
                [
                    convertButton
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    progressView = ft.Row(
        [
            ft.Column(
                [
                    progress
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
        )
    
    
    page.add(introView,
    selectView,
    spacer,
    selectFileView,
    spacer,
    filePickView,
    spacer,
    convertView,
    spacer,
    progressView)

# set app for desktop usage
ft.app(target=main)