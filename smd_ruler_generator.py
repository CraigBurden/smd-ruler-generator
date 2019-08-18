import ezdxf

def ruler_label(x, y, label, size):
    msp.add_text(
        str(label),
        dxfattribs={'rotation': 0,
                    'height': size,
                    'layer': 'SCAN'}
    ).set_pos((x, y - size/3))

def tick_label(x, y, label, size):
    msp.add_text(
        str(label),
        dxfattribs={'rotation': 90,
                    'height': size,
                    'layer': 'SCAN'}
    ).set_pos((x + size/3, y))

def ruler_tick(x, y, length, width, filled):
    if filled:
        ruler_tick = [(x, y),
                      (x, y + length),
                      (x + width, y + length),
                      (x + width, y),
                      (x, y)]
        msp.add_lwpolyline(ruler_tick, dxfattribs={'layer': 'SCAN'})
    else:
        msp.add_line((x, y), (x, y + length))

def ruler(label, start_y, pitch, count):

    ruler_label((start_x - ruler_label_offset), (start_y + (long_tick_length / 2)), label,  label_size)

    for index in range(1, count + 1):
        tick_x = start_x + ((index - 1) * pitch)

        if(index == 1):
            ruler_tick(tick_x, start_y, long_tick_length, tick_width, fill_ticks)
            tick_label(tick_x, (start_y + long_tick_length + 1), index, tick_label_size)
        elif((index % 10) == 0):                        # If this tick is a multiple of 10, draw a long line and label
            ruler_tick(tick_x, start_y, long_tick_length, tick_width, fill_ticks)
            tick_label(tick_x, (start_y + long_tick_length + 1), index, tick_label_size)
        elif((index % 5) == 0):                         # If this tick is a multiple of 5, draw a medium line
            ruler_tick(tick_x, start_y, mid_tick_length, tick_width, fill_ticks)
        else:                                           # Draw a short line
            ruler_tick(tick_x, start_y, short_tick_length, tick_width, fill_ticks)

def stacked_rulers(list, spacing):
    y = 0
    for element in list:
        ruler(element[0], y, element[1], element[2])
        y += spacing

dwg = ezdxf.new('R2010')
dwg.layers.new(name='CUT', dxfattribs={'color': 7})
dwg.layers.new(name='SCAN', dxfattribs={'color': 5})
msp = dwg.modelspace()

start_x = 0
short_tick_length = 2
mid_tick_length = 3
long_tick_length = 6
ruler_label_offset = 10
label_size = 3
tick_label_size = 1.5
tick_width = 0.01
fill_ticks = False

rulers = [
    ["0402", 2, 100],
    ["0603", 4, 100],
    ["0805", 4, 100],
    ["1206", 4, 100]
]

stacked_rulers(rulers, 10)

filename = 'ruler.dxf'
dwg.saveas(filename)
