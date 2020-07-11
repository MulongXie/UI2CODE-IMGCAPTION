import lib.img_drawLabel as draw
import lib.img_segment as seg
import lib.web_catchElementInfo as catch

import pandas as pd
from os.path import join as pjoin
import time
from func_timeout import func_set_timeout, FunctionTimedOut

start_time = time.clock()
is_segment = False
is_draw_label = True
# set the web crawler
driver_path = 'D:/webdriver'
url = "https://www.bbc.com/"
# set the format of label
libel_format = pd.read_csv('data/format.csv', index_col=0)

# catch label and screenshot img and segment them into smaller size
index = 0
out_dir = 'data'
img, label = None, None
catch_success = False
try:
    img, label = catch.catch(url, index, out_dir, libel_format, driver_path)

    # read and draw label on segment img
    if is_draw_label and img is not None and label is not None:
        img_drawn_path = pjoin(out_dir, str(index) + '_drawn.png')
        draw.label(label, img, img_drawn_path)
    # segment the lengthy images
    if is_segment and img is not None:
        img_segment_dir = pjoin(out_dir, str(index) + '/segment')
        seg.segment_img(img, 600, img_segment_dir, 0)

except FunctionTimedOut:
    print('Catch Time Out')

end_time = time.clock()
print("*** Time taken:%ds ***" % int(end_time - start_time))
