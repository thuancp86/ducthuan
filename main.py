# -*- coding: utf-8 -*-
# Module: default
# Author: Học Mãi Mãi.
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
VIDEOS = {'[COLOR pink]Onetv (Chỉ Mạng FPT)[/COLOR]': [{'name': '[COLOR fuchsia]V[COLOR lime]T[COLOR gold]V[COLOR pink]1 [COLOR white]HD[/COLOR]',
                       'thumb': 'http://i.imgur.com/DMLgaGv.jpg',
                       'video': 'udp://@225.1.2.249:30120',
                       'genre': 'Truyền Hình'},
                      {'name': '[COLOR lime]VTV3 HD[/COLOR]',
                       'thumb': 'http://i.imgur.com/POsorLa.jpg',
                       'video': 'udp://@225.1.2.247:30120',
                       'genre': 'Truyền Hình'},
					  {'name': '[COLOR gold]VTC13-iTV HD[/COLOR]',
                       'thumb': 'http://i.imgur.com/JoiOy9L.png',
                       'video': 'udp://@225.1.2.250:30120',
                       'genre': 'Truyền Hình'},
                      {'name': '[COLOR white]HBO HD[/COLOR]',
                       'thumb': 'http://i.imgur.com/J0Uju0r.png',
                       'video': 'udp://@225.1.2.233:30120',
                       'genre': 'Truyền Hình'}
                      ],
            'Phim': [{'name': 'Các vị thần ai cập',
                      'thumb': 'http://i.imgur.com/CkfHhnO.jpg',
                      'video': 'http://phim3s.net/phim-le/cac-vi-than-ai-cap_9050/xem-phim/240649/video.mp4',
                      'genre': 'Music'},
                     {'name': 'Con đường máu lửa',
                      'thumb': 'http://i.imgur.com/OdykeGa.jpg',
                      'video': 'http://phim3s.net/phim-le/con-duong-mau-lua_9045/xem-phim/240660/video.mp4',
                      'genre': 'Music'}
					  ],
			'Music': [{'name': 'ASIA 77',			 	 		  
                      'thumb': 'http://i.imgur.com/W7xFR6Q.jpg',
                      'video': 'http://www.mediafire.com/download/8fvc8pv43jwe46x/Asia77.Dong.Nhac.Anh.Bang.Va.Lam.Phuong.Bluray.1080p.mp4',
                      'genre': 'Music'},
                     {'name': 'PBN 117 Vườn hoa âm nhạc BlueRay HD',
                      'thumb': 'http://i.imgur.com/GgNxG9B.jpg',
                      'video': 'http://www.mediafire.com/watch/fj56quupoqr5d4b/Paris_By_Night_117_Vuon_Hoa_Am_Nhac_2016_mHD_BluRay_DD2.0_x264-TRiM.mp4',
                      'genre': 'Music'}		  
					  ],
			'[COLOR lime]Radio[/COLOR]': [{'name': '[COLOR rose]VOV1[/COLOR]',
                      'thumb': 'http://i.imgur.com/PEEbJUe.png',
                      'video': 'http://210.245.60.242:1935/vov1/vov1/playlist.m3u8',
                      'genre': 'Radio'},
                     {'name': '[COLOR white]VOV2[/COLOR]',
                      'thumb': 'http://i.imgur.com/T00Bqct.png',
                      'video': 'http://210.245.60.242:1935/vov2/vov2/playlist.m3u8',
                      'genre': 'Radio'},
					 {'name': '[COLOR tomato]VOV3[/COLOR]',
                      'thumb': 'http://i.imgur.com/jy8Nbdz.png',
                      'video': 'http://210.245.60.242:1935/vov3/vov3/playlist.m3u8',
                      'genre': 'Radio'},
                     {'name': '[COLOR khaki]Music Dance[/COLOR]',
                      'thumb': 'http://i.imgur.com/35eR0ta.jpg',
                      'video': 'http://95.141.24.61/',
                      'genre': 'Radio'}		  
                     ],
            '[COLOR gold]TV Tổng Hợp[/COLOR]': [{'name': '[COLOR lime]N+Live[/COLOR]',
                      'thumb': 'http://i.imgur.com/HzkTUxD.jpg',
                      'video': 'rtmp://123.30.134.108/live/nctlive',
                      'genre': 'TV Tổng Hợp'},
                     {'name': '[COLOR orange]KeengTV[/COLOR]',
                      'thumb': 'http://i.imgur.com/poqyVF8.jpg',
                      'video': 'http://125.235.29.16/livetv/keeng.m3u8',
                      'genre': 'TV Tổng Hợp'},
                     {'name': '[COLOR orangered]SCTVHD Phim Nước Ngoài[/COLOR]',
                      'thumb': 'http://i.imgur.com/ciNAHXZ.png',
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
