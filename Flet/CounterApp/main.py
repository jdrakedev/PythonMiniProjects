# In Flet widgets are referred to as controls

import flet as ft

# Create a flutter page instance
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK # LIGHT, DARK

    page.window_height = 400
    page.window_width = 400
    
    page.title = "Counter"
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # START, CENTER, END
    
    # Button logic
    def add(e):
        number.value = str(int(number.value) + 1)
        page.update()

    def subtract(e):
        number.value = str(int(number.value) - 1)
        page.update()

    # Create Controls instances
    number = ft.TextField(value='0', width=100, text_align=ft.TextAlign.CENTER)
    add_icon = ft.IconButton(icon=ft.icons.ADD, icon_color=ft.colors.TEAL, on_click=add)
    remove_icon = ft.IconButton(icon=ft.icons.REMOVE, icon_color=ft.colors.RED, on_click=subtract)
    
    # Add controls horizontally
    page.add(ft.Row(alignment=ft.MainAxisAlignment.SPACE_EVENLY, controls=[add_icon, number, remove_icon]))
    
    # Add controls vertically
    #page.add(remove_icon, number, add_icon)
    
    page.update()


# To view the app in the browser
#ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main)