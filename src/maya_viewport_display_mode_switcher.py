# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import maya.cmds as cmds

def viewport_display_mode_switcher(modes=('wireframe', 'points', 'boundingBox', 'smoothShaded', 'flatShaded', 'wireframeOnShaded')):
    """
    Switch display mode in the order specified by 'modes'.
    Available modes are as follows:
    ['wireframe', 'points', 'boundingBox', 'smoothShaded', 'flatShaded', 'wireframeOnShaded']

    Attributes:
        modes (list): list of display modes

    Returns:
        None

    Raises:
        ValueError: If the mode is invalid.
    """

    # Check if the modes are valid
    valid_modes = ['wireframe', 'points', 'boundingBox', 'smoothShaded', 'flatShaded', 'wireframeOnShaded']
    for mode in modes:
        if mode not in valid_modes:
            raise ValueError('Invalid mode: {0}'.format(mode))

    # get current panel
    current_panel = cmds.getPanel(withFocus=True)
    # get type of the panel
    panel_type = cmds.getPanel(typeOf=current_panel)
    # if the panel is not a modelPanel, do nothing
    if panel_type == "modelPanel":
        # get current display mode
        current_display_mode = cmds.modelEditor(current_panel, q=True, displayAppearance=True)
        is_wireframe_on_shaded = cmds.modelEditor(current_panel, q=True, wireframeOnShaded=True)
        if is_wireframe_on_shaded and (current_display_mode == 'smoothShaded'):
            current_display_mode = 'wireframeOnShaded'

        # get the index of the current display mode
        current_index = modes.index(current_display_mode)
        # get the next index (loop back if necessary)
        new_index = (current_index + 1) % len(modes)
        # get the new display mode
        new_mode = modes[new_index]

        # set the new display mode
        # if the new mode is 'wireframeOnShaded', set 'smoothShaded' first
        if new_mode == 'wireframeOnShaded':
            # set 'smoothShaded' first
            cmds.modelEditor(current_panel, e=True, displayAppearance='smoothShaded')
            # then set 'wireframeOnShaded'
            cmds.modelEditor(current_panel, e=True, wireframeOnShaded=True)
        else:
            if is_wireframe_on_shaded:
                # set 'wireframeOnShaded' off
                cmds.modelEditor(current_panel, e=True, wireframeOnShaded=False)
            # set the new display mode
            cmds.modelEditor(current_panel, e=True, displayAppearance=new_mode)

        # print the new display mode
        print('Now changed \'{0}\' mode.'.format(new_mode))

def execute(modes=('wireframe', 'points', 'boundingBox', 'smoothShaded', 'flatShaded', 'wireframeOnShaded')):
    viewport_display_mode_switcher(modes=modes)

if __name__ == '__main__':
    execute()
