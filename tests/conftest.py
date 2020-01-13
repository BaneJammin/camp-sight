import datetime

import pytest

# TODO: Develop test cases
dates = [
    {
        "start_str": "1\n1\n2020\n1\n",
        "start_date": datetime.date(2020, 1, 1),
        "end_date": datetime.date(2020, 1, 2),
        "window_dict": {
            "month": 1,
            "day": 1,
            "year": 2020,
            "emonth": 1,
            "eday": 2,
            "eyear": 2020,
            "find_pk": 1,
        },
    },
    {
        "start_str": "1\n31\n2020\n1\n",
        "start_date": datetime.date(2020, 1, 31),
        "end_date": datetime.date(2020, 2, 1),
        "window_dict": {
            "month": 1,
            "day": 31,
            "year": 2020,
            "emonth": 2,
            "eday": 1,
            "eyear": 2020,
            "find_pk": 1,
        },
    },
]


@pytest.fixture(params=dates)
def test_dates(request):
    return request.param


@pytest.fixture
def test_html():
    return """
        <!DOCTYPE html>
    <html lang="en-US">
       <head>
          <title>HTML Tables</title>
       </head>
       <body>
          <table cellpadding="3" cellspacing="0" style="border: solid 1px #c0c0c0; width: 100%; margin: 15px auto;">
             <colgroup>
                <col width="50%" />
                <col width="50%" />
             </colgroup>
             <tr>
                <td colspan="2" style="font-weight: bold; background-color: #C0C0C0;">Baker Road Park: : Baker Road Park Tent Camping</td>
             </tr>
             <tr>
                <td style="background-color: #eeeeee;">&nbsp;</td>
                <td style="text-align: center; background-color: #eeeeee; border-left: solid 1px #C0C0C0;">Sat, June 29, 2019 3:00 PM<br />Sun, June 30, 2019 12:00 PM</td>
             </tr>
             <tr style="">
                <td style="font-weight: bold; text-align: right; border-top: solid 1px #C0C0C0;">
                   <p align="center"><a href="/files/rooms/photos/Baker_Road_campsite_634x512_-_photo_by_Kevin_Vail.jpg" target="_blank"><img alt=": " height="121" src="/files/rooms/photos/Baker_Road_campsite_634x512_-_photo_by_Kevin_Vail_thumb.jpg" width="150" /></a></p>
                </td>
                <td style="vertical-align: middle;text-align: center; border-top: solid 1px #C0C0C0; border-left: solid 1px #C0C0C0; background-color: #990000; color: #FFFFFF;"> Reserved</td>
             </tr>
          </table>
          <table cellpadding="3" cellspacing="0" style="border: solid 1px #c0c0c0; width: 100%; margin: 15px auto;">
             <colgroup>
                <col width="50%" />
                <col width="50%" />
             </colgroup>
             <tr>
                <td colspan="2" style="font-weight: bold; background-color: #C0C0C0;">Blair Ridge Park: : Blair Ridge Park Tent Camping </td>
             </tr>
             <tr>
                <td style="background-color: #eeeeee;">&nbsp;</td>
                <td style="text-align: center; background-color: #eeeeee; border-left: solid 1px #C0C0C0;">Sat, June 29, 2019 3:00 PM<br />Sun, June 30, 2019 12:00 PM</td>
             </tr>
             <tr style="">
                <td style="font-weight: bold; text-align: right; border-top: solid 1px #C0C0C0;">
                   <p align="center"><a href="/files/rooms/photos/Blair-Ridge-Campsite-634.jpg" target="_blank"><img alt=": " height="121" src="/files/rooms/photos/Blair-Ridge-Campsite-634_thumb.jpg" width="150" /></a></p>
                </td>
                <td style="vertical-align: middle;text-align: center; border-top: solid 1px #C0C0C0; border-left: solid 1px #C0C0C0; background-color: #990000; color: #FFFFFF;"> Reserved</td>
             </tr>
          </table>
          <table cellpadding="3" cellspacing="0" style="border: solid 1px #c0c0c0; width: 100%; margin: 15px auto;">
             <colgroup>
                <col width="50%" />
                <col width="50%" />
             </colgroup>
             <tr>
                <td colspan="2" style="font-weight: bold; background-color: #C0C0C0;">Girdled Road Reservation: Area: Girdled Road Tent Camping</td>
             </tr>
             <tr>
                <td style="background-color: #eeeeee;">&nbsp;</td>
                <td style="text-align: center; background-color: #eeeeee; border-left: solid 1px #C0C0C0;">Sat, June 29, 2019 3:00 PM<br />Sun, June 30, 2019 12:00 PM</td>
             </tr>
             <tr style="">
                <td style="font-weight: bold; text-align: right; border-top: solid 1px #C0C0C0;">
                   <p align="center"><a href="/files/rooms/photos/Girdled_Road_Reservation_Campsite_634x512_-_photo_by_Kevin_Vail.jpg" target="_blank"><img alt=": " height="121" src="/files/rooms/photos/Girdled_Road_Reservation_Campsite_634x512_-_photo_by_Kevin_Vail_thumb.jpg" width="150" /></a></p>
                </td>
                <td style="vertical-align: middle;text-align: center; border-top: solid 1px #C0C0C0; border-left: solid 1px #C0C0C0; background-color: ; color: #000000;"> <a class="facilitybutton" href="?rm_id=381&amp;dt=MjAxOS0wNi0yOToyMDE5LTA2LTMw&amp;tp=1&amp;tk=503758.21236">Reserve now</a></td>
             </tr>
          </table>
          <table cellpadding="3" cellspacing="0" style="border: solid 1px #c0c0c0; width: 100%; margin: 15px auto;">
             <colgroup>
                <col width="50%" />
                <col width="50%" />
             </colgroup>
             <tr>
                <td colspan="2" style="font-weight: bold; background-color: #C0C0C0;">Hidden Lake: : Hidden Lake Tent Camping</td>
             </tr>
             <tr>
                <td style="background-color: #eeeeee;">&nbsp;</td>
                <td style="text-align: center; background-color: #eeeeee; border-left: solid 1px #C0C0C0;">Sat, June 29, 2019 3:00 PM<br />Sun, June 30, 2019 12:00 PM</td>
             </tr>
             <tr style="">
                <td style="font-weight: bold; text-align: right; border-top: solid 1px #C0C0C0;">
                   <p align="center"><a href="/files/rooms/photos/Hidden_Lake_Campsite_634x512_-_photo_by_Kevin_Vail.jpg" target="_blank"><img alt=": " height="121" src="/files/rooms/photos/Hidden_Lake_Campsite_634x512_-_photo_by_Kevin_Vail_thumb.jpg" width="150" /></a></p>
                </td>
                <td style="vertical-align: middle;text-align: center; border-top: solid 1px #C0C0C0; border-left: solid 1px #C0C0C0; background-color: #990000; color: #FFFFFF;"> Reserved</td>
             </tr>
          </table>
          <table cellpadding="3" cellspacing="0" style="border: solid 1px #c0c0c0; width: 100%; margin: 15px auto;">
             <colgroup>
                <col width="50%" />
                <col width="50%" />
             </colgroup>
             <tr>
                <td colspan="2" style="font-weight: bold; background-color: #C0C0C0;">Lake Erie Bluffs: Lane Road entrance: Tent Campsite A</td>
             </tr>
             <tr>
                <td style="background-color: #eeeeee;">&nbsp;</td>
                <td style="text-align: center; background-color: #eeeeee; border-left: solid 1px #C0C0C0;">Sat, June 29, 2019 3:00 PM<br />Sun, June 30, 2019 12:00 PM</td>
             </tr>
             <tr style="">
                <td style="font-weight: bold; text-align: right; border-top: solid 1px #C0C0C0;">
                   <p align="center"><a href="/files/rooms/photos/Lake_Erie_Bluffs_Campsite_A_web.jpg" target="_blank"><img alt=": " height="121" src="/files/rooms/photos/Lake_Erie_Bluffs_Campsite_A_web_thumb.jpg" width="150" /></a></p>
                </td>
                <td style="vertical-align: middle;text-align: center; border-top: solid 1px #C0C0C0; border-left: solid 1px #C0C0C0; background-color: #990000; color: #FFFFFF;"> Reserved</td>
             </tr>
          </table>
          <table cellpadding="3" cellspacing="0" style="border: solid 1px #c0c0c0; width: 100%; margin: 15px auto;">
             <colgroup>
                <col width="50%" />
                <col width="50%" />
             </colgroup>
             <tr>
                <td colspan="2" style="font-weight: bold; background-color: #C0C0C0;">Lake Erie Bluffs: Lane Road entrance: Tent Campsite B</td>
             </tr>
             <tr>
                <td style="background-color: #eeeeee;">&nbsp;</td>
                <td style="text-align: center; background-color: #eeeeee; border-left: solid 1px #C0C0C0;">Sat, June 29, 2019 3:00 PM<br />Sun, June 30, 2019 12:00 PM</td>
             </tr>
             <tr style="">
                <td style="font-weight: bold; text-align: right; border-top: solid 1px #C0C0C0;">
                   <p align="center"><a href="/files/rooms/photos/Lake_Erie_Bluffs_tent_campsite_B_634x512.jpg" target="_blank"><img alt=": " height="121" src="/files/rooms/photos/Lake_Erie_Bluffs_tent_campsite_B_634x512_thumb.jpg" width="150" /></a></p>
                </td>
                <td style="vertical-align: middle;text-align: center; border-top: solid 1px #C0C0C0; border-left: solid 1px #C0C0C0; background-color: #990000; color: #FFFFFF;"> Reserved</td>
             </tr>
          </table>
          <table cellpadding="3" cellspacing="0" style="border: solid 1px #c0c0c0; width: 100%; margin: 15px auto;">
             <colgroup>
                <col width="50%" />
                <col width="50%" />
             </colgroup>
             <tr>
                <td colspan="2" style="font-weight: bold; background-color: #C0C0C0;">Lakeshore Reservation: Area: Lakeshore Reservation Tent Camping</td>
             </tr>
             <tr>
                <td style="background-color: #eeeeee;">&nbsp;</td>
                <td style="text-align: center; background-color: #eeeeee; border-left: solid 1px #C0C0C0;">Sat, June 29, 2019 3:00 PM<br />Sun, June 30, 2019 12:00 PM</td>
             </tr>
             <tr style="">
                <td style="font-weight: bold; text-align: right; border-top: solid 1px #C0C0C0;">
                   <p align="center"><a href="/files/rooms/photos/Lakeshore_Reservation_tent_campsite_634x512.jpg" target="_blank"><img alt=": " height="121" src="/files/rooms/photos/Lakeshore_Reservation_tent_campsite_634x512_thumb.jpg" width="150" /></a></p>
                </td>
                <td style="vertical-align: middle;text-align: center; border-top: solid 1px #C0C0C0; border-left: solid 1px #C0C0C0; background-color: #990000; color: #FFFFFF;"> Reserved</td>
             </tr>
          </table>
          <table cellpadding="3" cellspacing="0" style="border: solid 1px #c0c0c0; width: 100%; margin: 15px auto;">
             <colgroup>
                <col width="50%" />
                <col width="50%" />
             </colgroup>
             <tr>
                <td colspan="2" style="font-weight: bold; background-color: #C0C0C0;">Penitentiary Glen Reservation: Area: Penitentiary Glen Reservation Tent Camping</td>
             </tr>
             <tr>
                <td style="background-color: #eeeeee;">&nbsp;</td>
                <td style="text-align: center; background-color: #eeeeee; border-left: solid 1px #C0C0C0;">Sat, June 29, 2019 3:00 PM<br />Sun, June 30, 2019 12:00 PM</td>
             </tr>
             <tr style="">
                <td style="font-weight: bold; text-align: right; border-top: solid 1px #C0C0C0;">
                   <p align="center"><a href="/files/rooms/photos/Penitentiary_Glen_Reservation_campsite_1920x1080_-_photo_by_Kevin_Vail.jpg" target="_blank"><img alt=": " height="84" src="/files/rooms/photos/Penitentiary_Glen_Reservation_campsite_1920x1080_-_photo_by_Kevin_Vail_thumb.jpg" width="150" /></a></p>
                </td>
                <td style="vertical-align: middle;text-align: center; border-top: solid 1px #C0C0C0; border-left: solid 1px #C0C0C0; background-color: #990000; color: #FFFFFF;"> Reserved</td>
             </tr>
          </table>
          <table cellpadding="3" cellspacing="0" style="border: solid 1px #c0c0c0; width: 100%; margin: 15px auto;">
             <colgroup>
                <col width="50%" />
                <col width="50%" />
             </colgroup>
             <tr>
                <td colspan="2" style="font-weight: bold; background-color: #C0C0C0;">River Road Park - Area: : River Road Park Tent Camping</td>
             </tr>
             <tr>
                <td style="background-color: #eeeeee;">&nbsp;</td>
                <td style="text-align: center; background-color: #eeeeee; border-left: solid 1px #C0C0C0;">Sat, June 29, 2019 3:00 PM<br />Sun, June 30, 2019 12:00 PM</td>
             </tr>
             <tr style="">
                <td style="font-weight: bold; text-align: right; border-top: solid 1px #C0C0C0;">
                   <p align="center"><a href="/files/rooms/photos/River_Road_Park_campsite_634x512.jpg" target="_blank"><img alt=": " height="121" src="/files/rooms/photos/River_Road_Park_campsite_634x512_thumb.jpg" width="150" /></a></p>
                </td>
                <td style="vertical-align: middle;text-align: center; border-top: solid 1px #C0C0C0; border-left: solid 1px #C0C0C0; background-color: ; color: #000000;"> <a class="facilitybutton" href="?rm_id=381&amp;dt=MjAxOS0wNi0yOToyMDE5LTA2LTMw&amp;tp=1&amp;tk=503758.21236">Reserve now</a></td>
             </tr>
          </table>
          <table cellpadding="3" cellspacing="0" style="border: solid 1px #c0c0c0; width: 100%; margin: 15px auto;">
             <colgroup>
                <col width="50%" />
                <col width="50%" />
             </colgroup>
             <tr>
                <td colspan="2" style="font-weight: bold; background-color: #C0C0C0;">Riverview Park: Area: Riverview Park Tent Camping</td>
             </tr>
             <tr>
                <td style="background-color: #eeeeee;">&nbsp;</td>
                <td style="text-align: center; background-color: #eeeeee; border-left: solid 1px #C0C0C0;">Sat, June 29, 2019 3:00 PM<br />Sun, June 30, 2019 12:00 PM</td>
             </tr>
             <tr style="">
                <td style="font-weight: bold; text-align: right; border-top: solid 1px #C0C0C0;">
                   <p align="center"><a href="/files/rooms/photos/Riverview_Campsite_1920x1080_-_photo_by_Kevin_Vail.jpg" target="_blank"><img alt=": " height="84" src="/files/rooms/photos/Riverview_Campsite_1920x1080_-_photo_by_Kevin_Vail_thumb.jpg" width="150" /></a></p>
                </td>
                <td style="vertical-align: middle;text-align: center; border-top: solid 1px #C0C0C0; border-left: solid 1px #C0C0C0; background-color: #990000; color: #FFFFFF;"> Reserved</td>
             </tr>
          </table>
       </body>
    </html>
    """
