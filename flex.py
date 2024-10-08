import time

import flet
from flet import Page, Container, LinearGradient, alignment, Column, Row, padding, Text, \
    MainAxisAlignment, ResponsiveRow, PopupMenuButton, PopupMenuItem, IconButton, icons, transform, \
    animation


def main(page: Page):
    page.title = "Flexible page"

    def on_resize(e):
        if page.width <= 730:
            _nav.controls[0].visible = False
            # _nav.update()
            _min_nav.visible = True
        else:
            _min_nav.visible = False
            _nav.controls[0].visible = True
        _nav.update()
        _min_nav.update()

    page.on_resize = on_resize

    def _change_text_color(e):

        if e.control.content.color == "white":
            e.control.content.color = "red"
        else:
            e.control.content.color = "white"
        e.control.content.update()

    _items = [f"ITEM {i}" for i in range(1, 7)]
    _item_row = ResponsiveRow(alignment="start", spacing=20)
    _container_item = Container(
        content=_item_row,
        padding=20
    )
    for item in _items:
        _item_container = Container(
            aspect_ratio=1, bgcolor="white", padding=35, border_radius=12,
            alignment=alignment.center,
            col={"xs": 12, "sm": 4, "md": 4, "lg": 6, "xl": 4},
            content=Container(aspect_ratio=1, border_radius=8, alignment=alignment.center,
                              bgcolor="black",
                              content=Text(item, size=21, weight="w600"))
        )
        _item_row.controls.append(_item_container)
    _nav = Row(
        alignment=MainAxisAlignment.END,
        controls=[
            Container(
                padding=padding.only(right=20),
                # bgcolor="pink",
                height=64,
                content=Row(controls=[
                    Container(
                        on_hover=_change_text_color,
                        content=Text(
                            "About me",
                            # width="w600",
                            color="white")),
                    Container(
                        on_hover=_change_text_color,
                        content=Text(
                            "Contact",
                            # width="w600",
                            color="white")),
                    Container(

                        on_hover=_change_text_color,
                        content=Text(
                            "Services",
                            # width="w600",
                            color="white")),
                ]
                )
            )

        ]
    )
    _min_nav = Row(
        visible=False,
        controls=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="About me", ),
                    PopupMenuItem(text="Contact", ),
                    PopupMenuItem(text="Services", ),
                ]
            )
        ]
    )

    _sub_title = ResponsiveRow(
        alignment="center",
        controls=[
            Container(
                col={"xs": 12, "sm": 10, "md": 10, "lg": 10, "xl": 12},
                padding=20,
                alignment=alignment.top_center,
                content=Text(
                    "Welcome to my personal flet project\nHave a look around and contact me if"
                    "you find something  interesting!",
                    text_align="center",
                    size=16,
                    weight="w500",
                    color="white"
                )
            )
        ]
    )
    _title = ResponsiveRow(
        alignment="center",
        controls=[
            Container(
                col={"xs": 12, "sm": 10, "md": 10, "lg": 10, "xl": 12},
                alignment=alignment.top_center,
                padding=20,
                content=Text(
                    "My portfolio\nflexable app in flet",
                    size=45,
                    weight="w600",
                    color="white",
                    text_align="center",
                )
            )
        ]
    )
    _icon_list = [
        icons.FACEBOOK,
        icons.SHARE_SHARP,
        icons.TIKTOK,
    ]

    _social_button = Row(
        alignment="center",
        vertical_alignment="center"
    )
    _icon_text = Text(
        "Connect!",
        size=16,
        color="white",
        animate_opacity=50,
        weight='w800',
        offset=transform.Offset(0, -1.1),
        animate_offset=animation.Animation(duration=1000, curve="elasticOut"),

    )
    for icon in _icon_list:
        _icon = IconButton(icon=icon,
                           icon_size=22,
                           icon_color="white",
                           offset=transform.Offset(0, -0.9),
                           animate_offset=animation.Animation(duration=1000, curve="elasticOut"),
                           animate_opacity=50,
                           opacity=0
                           )
        _social_button.controls.append(_icon)

    def _animate_social(e):
        if e.data == "true":
            _icon_text.offset, _icon_text.opacity = transform.Offset(0, 0.05), 0
            _icon_text.update()
            for btn in _social_button.controls[:]:
                btn.offset, btn.opacity = transform.Offset(0, 0.15), 100
                btn.update()
                time.sleep(0.1)

        else:
            for btn in _social_button.controls[:]:
                btn.offset, btn.opacity = transform.Offset(0, -0.9), 0
                btn.update()
                time.sleep(0.1)
            _icon_text.offset, _icon_text.opacity = transform.Offset(0, -1.1), 100
            _icon_text.update()

    _icon_container = Container(
        width=145,
        height=50,
        bgcolor="blue800",
        alignment=alignment.center,
        border_radius=8,
        on_hover=_animate_social,
        on_click=_animate_social,
        content=Column(
            spacing=0,
            alignment="center",
            horizontal_alignment="center",

            controls=[_social_button,
                      Row(
                          alignment="center",
                          controls=[_icon_text])
                      ],
        )
    )
    _main_col = Column(horizontal_alignment="center", scroll="auto")
    _main_col.controls.append(_nav)
    _main_col.controls.append(_min_nav)
    _main_col.controls.append(_title)
    _main_col.controls.append(_sub_title)
    _main_col.controls.append(Container(padding=padding.only(top=10)))
    _main_col.controls.append(_icon_container)
    _main_col.controls.append(Container(padding=padding.only(bottom=40)))
    _main_col.controls.append(_container_item)
    _background = Container(margin=-10,
                            height=page.height,
                            expand=True,
                            content=_main_col,
                            gradient=LinearGradient(
                                begin=alignment.bottom_left,
                                end=alignment.top_right,
                                colors=["#13547a", "#000000"],

                            ))

    page.add(_background)


if __name__ == "__main__":
    flet.app(target=main)
