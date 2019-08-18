$fn = 1000;
font = "Lato:style=Hairline";
start_x = 0;
short_tick_length = 2;
mid_tick_length = 3;
long_tick_length = 6;
label_size = 3;
tick_label_size = 1.5;
tick_width = 0.01;

rulers = [
    ["0402", 2, 100],
    ["0603", 4, 100],
    ["0805", 4, 100],
    ["1206", 4, 100]
];

stacked_rulers(rulers, 10);

module stacked_rulers(list, spacing)
{
    y = 0;
    index = 0;
    for(index  = [0 : (len(list) - 1)])
    {
        ruler(list[index][0], y, list[index][1], list[index][2]);
        y = y + (index * spacing);
    }
}

module ruler(label, start_y, pitch, count)
{
    ruler_label((start_x - 2), (start_y + (long_tick_length / 2)), label,  label_size);
    
    for(index = [1 : count])
    {
        tick_x = start_x + ((index - 1) * pitch);
        
        if(index == 1)
        {
            vertical_line(tick_x, start_y, long_tick_length, tick_width);
            tick_label(tick_x, (start_y + long_tick_length + 1), index, tick_label_size);
        }
        else if((index % 10) == 0)                   // If this tick is a multiple of 10, draw a long line and label
        {
            vertical_line(tick_x, start_y, long_tick_length, tick_width);
            tick_label(tick_x, (start_y + long_tick_length + 1), index, tick_label_size);
        }
        else if((index % 5) == 0)          // If this tick is a multiple of 5, draw a medium line
        {
            vertical_line(tick_x, start_y, mid_tick_length, tick_width);
        }
        else                                                 // Draw a short line
        {
            vertical_line(tick_x, start_y, short_tick_length, tick_width);
        }
    }
}

module ruler_label(x, y, label, size)
{
    translate([x, y, 0])
        text(text = str(label), font = font, size = size, halign = "right", valign = "center");
}

module tick_label(x, y, label, size)
{
    translate([x, y, 0])
        text(text = str(label), font = font, size = size, halign = "center", valign = "bottom");
}

module vertical_line(x, y, length, width)
{
    translate([(x - (width/2)), y, 0])
        square([width, length], false);
}
