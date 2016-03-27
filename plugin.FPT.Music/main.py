# -*- coding: utf-8 -*-
# Module: default
# Author: Thuận.
# Created on: 26.3.2016
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'Onetv (Chỉ Mạng FPT)': [{'name': 'VTV1 HD',
                       'thumb': 'http://download028.fshare.vn/dl/kQRrpyuRtQ7DiFzzEcm+SUZYGG+5Z23oqguklwDwaujX2PEdzCywzxIE1SKeMk+36Eju21tan76S3v-4/VTV1%20HD.jpg',
                       'video': 'udp://@225.1.2.249:30120',
                       'genre': 'Truyền Hình'},
                      {'name': 'VTV3 HD',
                       'thumb': 'http://download031.fshare.vn/dl/jsCm246bVbhwWBK6o4TaTmGoYOQJykiJdEwNjcvH6LExC4XVKvymtf0zXB46BrZVVVenemIlyYb98A-v/VTV3%20HD.jpg',
                       'video': 'udp://@225.1.2.247:30120',
                       'genre': 'Truyền Hình'},
					  {'name': 'VTC13-iTV HD',
                       'thumb': 'http://download031.fshare.vn/dl/DNU4sjHs3jXp-amJKioTxH7TpqaQl3xYSirH1z+EvlikStP6At+LYKGmNjuCLHft5c1fgIG6CSSw8iQx/ITV%20HD.png',
                       'video': 'udp://@225.1.2.250:30120',
                       'genre': 'Truyền Hình'},
                      {'name': 'HBO HD',
                       'thumb': 'http://download028.fshare.vn/dl/oWokKZrk6wOeIZHIppbj9kQvoMPAlwO8pZqUSoJ0YnjOPj2XRslw1Hp3kJP-qSMY7VodC0KitXlKy6Yy/HBO%20HD.jpg',
                       'video': 'udp://@225.1.2.233:30120',
                       'genre': 'Truyền Hình'}
                      ],
            'Phim': [{'name': 'Vị Khách Ngoài Hành Tinh',
                      'thumb': 'http://download021.fshare.vn/dl/gmvxsmUxjqOHL-7aYCtwq6UWEC5mHv3xX1L2MHRLtc8GvyPBqV6jq-KgjI2MZrks8uUDbo-tn3olFzBm/V%E1%BB%8B%20Kh%C3%A1ch%20Ngo%C3%A0i%20H%C3%A0nh%20Tinh.jpg',
                      'video': 'http://f-14-vip.vn-hd.com/37546aca196249c58c2fd0c3a4d51471/hdviet/_definst_/smil:mp4_03/store_01_2016/12012016/Impossible_2015_720p_WEBDL_ViE/Impossible_2015_720p_WEBDL_ViE_TM.smil/media_b2500000_4.m3u8',
                      'genre': 'Music'},
                     {'name': 'Sử Thi Baahubali',
                      'thumb': 'http://download006.fshare.vn/dl/-JOnbmNPpp05QI5eobQhaAtHtbDIwibjwE9BHgv+ao0wV8fEFmUP2U7ADLasCDUocACsz1kSQC00WO1s/S%E1%BB%AD%20Thi%20Baahubali.jpg',
                      'video': 'http://n02.vn-hd.com/556028eb763f015ec57f3b4122d35ef0/082015/20/Baahubali_The_Beginning_2015_1080p_AC3_S/Baahubali_The_Beginning_2015_1080p_AC3_S_1792/playlist.m3u8',
                      'genre': 'Music'}
					  ],
			'Radio': [{'name': 'VOV1',
                      'thumb': 'http://download031.fshare.vn/dl/n9CV1hrIzx1oKmLnffDd1l-A+5KP7D93IyHge6Kon8e2zAf7X6S6gFc2TQGjgD0OwNIoseiEMHYW1v2t/VOV1.png',
                      'video': 'http://210.245.60.242:1935/vov1/vov1/playlist.m3u8',
                      'genre': 'Radio'},
                     {'name': 'VOV2',
                      'thumb': 'http://download029.fshare.vn/dl/AkoHoOCS1CDGFpv5PwyFmcGu3+4moLPKsooPppSjk2FodMvAyr6DyyqorCt3r6PP9f3d7A0N-KD74izk/VOV2.png',
                      'video': 'http://210.245.60.242:1935/vov2/vov2/playlist.m3u8',
                      'genre': 'Radio'},
					 {'name': 'VOV3',
                      'thumb': 'http://download027.fshare.vn/dl/CPn2AhDhAaGwVGWetWY71wmuTzF+e1NW1pTpt74-8wbpFABtMaw7ER2Ft0xXoM3-jEMUkOmqakz86FqI/VOV3.png',
                      'video': 'http://210.245.60.242:1935/vov3/vov3/playlist.m3u8',
                      'genre': 'Radio'},
                     {'name': 'Music Dance',
                      'thumb': 'http://download029.fshare.vn/dl/ae8BxcEhBg4MkFkWIWJNRdZtirKA8jXZMkJDNm5-kqMt3r6yFHWz9aFRFMj3CowzTC6FsBOntooOKx57/Music%20Dance.jpg',
                      'video': 'http://95.141.24.61/',
                      'genre': 'Radio'}		  
                     ],
            'TV Tổng Hợp': [{'name': 'N+LIVE',
                      'thumb': 'http://download031.fshare.vn/dl/woGoYX-0wA8p002FqkE9CRUg3oiYh5+sxXCEfdHKSmECsqBvyuzBo2SHXLa27NH1UhQRuyILjbnRc2nh/NLive.png',
                      'video': 'rtmp://123.30.134.108/live/nctlive',
                      'genre': 'TV Tổng Hợp'},
                     {'name': 'KeengTV',
                      'thumb': 'http://download029.fshare.vn/dl/TY7Em00YXu2osC6ejN0J-DMgy0k9f4EuhzZ+cxZeprBAqz1eb6y+CWHBjQSYS0zwn7dVoQc+TwEUDl1y/Keeng%20TV.jpg',
                      'video': 'http://125.235.29.16/livetv/keeng.m3u8',
                      'genre': 'TV Tổng Hợp'},
                     {'name': 'SCTVHD Phim Nước Ngoài',
                      'thumb': 'http://download029.fshare.vn/dl/Cpj05kJtTqwcw2rZH+sRD99K6-z9PXgxfeVXyKcz1SNVh5eVUYlBQqia084O5hZrZArbXQQTMGth9SpJ/SCTV%20HD%20-%20Phim%20N%C6%B0%E1%BB%9Bc%20Ngo%C3%A0i.png',
                      'video': 'rtmp://112.197.2.135:1935/colive/C015_HD_2',
                      'genre': 'TV Tổng Hợp'}
                     ]}		 


def get_categories():
    """
    Get the list of video categories.
    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    :return: list
    """
    return VIDEOS.keys()


def get_videos(category):
    """
    Get the list of videofiles/streams.
    Here you can insert some parsing code that retrieves
    the list of videostreams in a given category from some site or server.

    :param category: str
    :return: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Get video categories
    categories = get_categories()
    # Create a list for our items.
    listing = []
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category, thumbnailImage=VIDEOS[category][0]['thumb'])
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # http://mirrors.xbmc.org/docs/python-docs/15.x-isengard/xbmcgui.html#ListItem-setInfo
        list_item.setInfo('video', {'title': category, 'genre': category})
        # Create a URL for the plugin recursive callback.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = '{0}?action=listing&category={1}'.format(_url, category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the listing as a 3-element tuple.
        listing.append((url, list_item, is_folder))
    # Add our listing to Kodi.
    # Large lists and/or slower systems benefit from adding all items at once via addDirectoryItems
    # instead of adding one by ove via addDirectoryItem.
    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: str
    """
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Create a list for our items.
    listing = []
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        list_item.setInfo('video', {'title': video['name'], 'genre': video['genre']})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for the plugin recursive callback.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/vids/crab.mp4
        url = '{0}?action=play&video={1}'.format(_url, video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the listing as a 3-element tuple.
        listing.append((url, list_item, is_folder))
    # Add our listing to Kodi.
    # Large lists and/or slower systems benefit from adding all items at once via addDirectoryItems
    # instead of adding one by ove via addDirectoryItem.
    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring:
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
