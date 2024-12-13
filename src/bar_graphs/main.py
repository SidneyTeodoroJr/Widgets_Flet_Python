import flet as ft

def main(page:ft.Page):
    page.theme_mode= ft.ThemeMode.DARK
    page.title= "Bar Graphs"
    bar= ft.BarChart(
        max_y=100,
        expand=True,
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.WHITE24,
            dash_pattern=[3,3],
           interval=5,
            width=1

        ),
        border=ft.border.all(width=1, color=ft.colors.WHITE),
        left_axis=ft.ChartAxis(
            title=ft.Text("Teste Bar", color=ft.colors.GREEN, selectable=True),
            labels_size=30
        ),

        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=1, label=ft.Container(ft.Text("Label 1"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=2, label=ft.Container(ft.Text("Label 2"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=3, label=ft.Container(ft.Text("Label 3"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=4, label=ft.Container(ft.Text("Label 4"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=5, label=ft.Container(ft.Text("Label 4"), padding=10)
                )
            ],
            labels_size=40
        ),
        tooltip_bgcolor=ft.colors.SURFACE_VARIANT,
        bar_groups=[
            ft.BarChartGroup(
                x= 2,
                bar_rods=[
                    ft.BarChartRod(
                        from_y= 0,
                        to_y= 40,
                        width=30,
                        color=ft.colors.RED_600,
                        border_radius=0,
                        tooltip="2"
                    )
                ]
            ),
            ft.BarChartGroup(
                x= 1,
                bar_rods=[
                    ft.BarChartRod(
                        from_y= 0,
                        to_y= 35,
                        width=30,
                        color=ft.colors.ORANGE_300,
                        border_radius=0,
                        tooltip="1"
                    )
                ]
            ),
            ft.BarChartGroup(
                x= 3,
                bar_rods=[
                    ft.BarChartRod(
                        from_y= 0,
                        to_y= 20,
                        width=30,
                        color=ft.colors.GREEN_400,
                        border_radius=0,
                        tooltip="3"
                    )
                ]
            ),
            ft.BarChartGroup(
                x= 4,
                bar_rods=[
                    ft.BarChartRod(
                        from_y= 0,
                        to_y= 57,
                        width=30,
                        color=ft.colors.PURPLE_100,
                        border_radius=0,
                        tooltip="4"
                    )
                ]
            ),
            ft.BarChartGroup(
                x= 5,
                bar_rods=[
                    ft.BarChartRod(
                        from_y= 0,
                        to_y= 17,
                        width=30,
                        color=ft.colors.PINK_900,
                        border_radius=0,
                        tooltip="4"
                    )
                ]
            )

        ]
    )

    page.add(
        bar
    )

    page.update()
ft.app(target=main)