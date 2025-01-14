# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import newgrounds


__tests__ = (
{
    "#url"     : "https://www.newgrounds.com/art/view/tomfulp/ryu-is-hawt",
    "#category": ("", "newgrounds", "image"),
    "#class"   : newgrounds.NewgroundsImageExtractor,
    "#sha1_url"    : "57f182bcbbf2612690c3a54f16ffa1da5105245e",
    "#sha1_content": "8f395e08333eb2457ba8d8b715238f8910221365",

    "artist"     : ["tomfulp"],
    "comment"    : r"re:Consider this the bottom threshold for ",
    "date"       : "dt:2009-06-04 14:44:05",
    "description": r"re:Consider this the bottom threshold for ",
    "favorites"  : int,
    "filename"   : "94_tomfulp_ryu-is-hawt",
    "height"     : 476,
    "index"      : 94,
    "rating"     : "e",
    "score"      : float,
    "tags"       : [
        "ryu",
        "streetfighter",
    ],
    "title"      : "Ryu is Hawt",
    "type"       : "article",
    "user"       : "tomfulp",
    "width"      : 447,
},

{
    "#url"     : "https://art.ngfiles.com/images/0/94_tomfulp_ryu-is-hawt.gif",
    "#category": ("", "newgrounds", "image"),
    "#class"   : newgrounds.NewgroundsImageExtractor,
    "#sha1_url": "57f182bcbbf2612690c3a54f16ffa1da5105245e",
},

{
    "#url"     : "https://www.newgrounds.com/art/view/sailoryon/yon-dream-buster",
    "#category": ("", "newgrounds", "image"),
    "#class"   : newgrounds.NewgroundsImageExtractor,
    "#count"   : 2,
    "#sha1_url": "84eec95e663041a80630df72719f231e157e5f5d",
},

{
    "#url"     : "https://www.newgrounds.com/art/view/kekiiro/red",
    "#comment" : "'adult' rated (#2456)",
    "#category": ("", "newgrounds", "image"),
    "#class"   : newgrounds.NewgroundsImageExtractor,
    "#options" : {"username": None},
    "#count"   : 1,
},

{
    "#url"     : "https://www.newgrounds.com/portal/view/595355",
    "#category": ("", "newgrounds", "media"),
    "#class"   : newgrounds.NewgroundsMediaExtractor,
    "#pattern" : r"https://uploads\.ungrounded\.net/alternate/564000/564957_alternate_31\.mp4\?1359712249",

    "artist"     : [
        "kickinthehead",
        "danpaladin",
        "tomfulp",
    ],
    "comment"    : r"re:My fan trailer for Alien Hominid HD!",
    "date"       : "dt:2013-02-01 09:50:49",
    "description": "Fan trailer for Alien Hominid HD!",
    "favorites"  : int,
    "filename"   : "564957_alternate_31",
    "index"      : 595355,
    "rating"     : "e",
    "score"      : float,
    "tags"       : [
        "alienhominid",
        "trailer",
    ],
    "title"      : "Alien Hominid Fan Trailer",
    "type"       : "movie",
    "user"       : "kickinthehead",
},

{
    "#url"     : "https://www.newgrounds.com/audio/listen/609768",
    "#category": ("", "newgrounds", "media"),
    "#class"   : newgrounds.NewgroundsMediaExtractor,
    "#sha1_url": "f4c5490ae559a3b05e46821bb7ee834f93a43c95",

    "artist"     : [
        "zj",
        "tomfulp",
    ],
    "comment"    : r"""re:RECORDED 12-09-2014

From The ZJ "Late """,
    "date"       : "dt:2015-02-23 19:31:59",
    "description": "From The ZJ Report Show!",
    "favorites"  : int,
    "index"      : 609768,
    "rating"     : "",
    "score"      : float,
    "tags"       : [
        "fulp",
        "interview",
        "tom",
        "zj",
    ],
    "title"      : "ZJ Interviews Tom Fulp!",
    "type"       : "music.song",
    "user"       : "zj",
},

{
    "#url"     : "https://www.newgrounds.com/portal/view/161181/format/flash",
    "#comment" : "flash animation (#1257)",
    "#category": ("", "newgrounds", "media"),
    "#class"   : newgrounds.NewgroundsMediaExtractor,
    "#pattern" : r"https://uploads\.ungrounded\.net/161000/161181_ddautta_mask__550x281_\.swf\?f1081628129",

    "type": "movie",
},

{
    "#url"     : "https://www.newgrounds.com/portal/view/758545",
    "#comment" : "format selection (#1729)",
    "#category": ("", "newgrounds", "media"),
    "#class"   : newgrounds.NewgroundsMediaExtractor,
    "#options" : {"format": "720p"},
    "#pattern" : r"https://uploads\.ungrounded\.net/alternate/1482000/1482860_alternate_102516\.720p\.mp4\?\d+",
},

{
    "#url"     : "https://www.newgrounds.com/portal/view/717744",
    "#comment" : "'adult' rated (#2456)",
    "#category": ("", "newgrounds", "media"),
    "#class"   : newgrounds.NewgroundsMediaExtractor,
    "#options" : {"username": None},
    "#count"   : 1,
},

{
    "#url"     : "https://www.newgrounds.com/portal/view/829032",
    "#comment" : "flash game",
    "#category": ("", "newgrounds", "media"),
    "#class"   : newgrounds.NewgroundsMediaExtractor,
    "#pattern" : r"https://uploads\.ungrounded\.net/829000/829032_picovsbeardx\.swf\?f1641968445",
    "#range"   : "1",

    "artist"     : [
        "dungeonation",
        "carpetbakery",
        "animalspeakandrews",
        "bill",
        "chipollo",
        "dylz49",
        "gappyshamp",
        "pinktophat",
        "rad",
        "shapeshiftingblob",
        "tomfulp",
        "voicesbycorey",
        "psychogoldfish",
    ],
    "comment"    : r"re:The children are expendable. Take out the ",
    "date"       : "dt:2022-01-10 23:00:57",
    "description": "Bloodshed in The Big House that Blew...again!",
    "favorites"  : int,
    "index"      : 829032,
    "post_url"   : "https://www.newgrounds.com/portal/view/829032",
    "rating"     : "m",
    "score"      : float,
    "tags"       : [
        "assassin",
        "boyfriend",
        "darnell",
        "nene",
        "pico",
        "picos-school",
    ],
    "title"      : "PICO VS BEAR DX",
    "type"       : "game",
    "url"        : "https://uploads.ungrounded.net/829000/829032_picovsbeardx.swf?f1641968445",
},

{
    "#url"     : "https://tomfulp.newgrounds.com/art",
    "#category": ("", "newgrounds", "art"),
    "#class"   : newgrounds.NewgroundsArtExtractor,
    "#pattern" : newgrounds.NewgroundsImageExtractor.pattern,
    "#count"   : ">= 3",
},

{
    "#url"     : "https://tomfulp.newgrounds.com/audio",
    "#category": ("", "newgrounds", "audio"),
    "#class"   : newgrounds.NewgroundsAudioExtractor,
    "#pattern" : r"https://audio.ngfiles.com/\d+/\d+_.+\.mp3",
    "#count"   : ">= 4",
},

{
    "#url"     : "https://tomfulp.newgrounds.com/movies",
    "#category": ("", "newgrounds", "movies"),
    "#class"   : newgrounds.NewgroundsMoviesExtractor,
    "#pattern" : r"https://uploads.ungrounded.net(/alternate)?/\d+/\d+_.+",
    "#range"   : "1-10",
    "#count"   : 10,
},

{
    "#url"     : "https://tomfulp.newgrounds.com/games",
    "#category": ("", "newgrounds", "games"),
    "#class"   : newgrounds.NewgroundsGamesExtractor,
    "#pattern" : r"https://uploads.ungrounded.net(/alternate)?/\d+/\d+_.+",
    "#range"   : "1-10",
    "#count"   : 10,
},

{
    "#url"     : "https://tomfulp.newgrounds.com",
    "#category": ("", "newgrounds", "user"),
    "#class"   : newgrounds.NewgroundsUserExtractor,
    "#pattern" : "https://tomfulp.newgrounds.com/art$",
},

{
    "#url"     : "https://tomfulp.newgrounds.com",
    "#category": ("", "newgrounds", "user"),
    "#class"   : newgrounds.NewgroundsUserExtractor,
    "#options" : {"include": "all"},
    "#pattern" : "https://tomfulp.newgrounds.com/(art|audio|movies)$",
    "#count"   : 3,
},

{
    "#url"     : "https://tomfulp.newgrounds.com/favorites/art",
    "#category": ("", "newgrounds", "favorite"),
    "#class"   : newgrounds.NewgroundsFavoriteExtractor,
    "#range"   : "1-10",
    "#count"   : ">= 10",
},

{
    "#url"     : "https://tomfulp.newgrounds.com/favorites/audio",
    "#category": ("", "newgrounds", "favorite"),
    "#class"   : newgrounds.NewgroundsFavoriteExtractor,
},

{
    "#url"     : "https://tomfulp.newgrounds.com/favorites/movies",
    "#category": ("", "newgrounds", "favorite"),
    "#class"   : newgrounds.NewgroundsFavoriteExtractor,
},

{
    "#url"     : "https://tomfulp.newgrounds.com/favorites/",
    "#category": ("", "newgrounds", "favorite"),
    "#class"   : newgrounds.NewgroundsFavoriteExtractor,
},

{
    "#url"     : "https://tomfulp.newgrounds.com/favorites/following",
    "#category": ("", "newgrounds", "following"),
    "#class"   : newgrounds.NewgroundsFollowingExtractor,
    "#pattern" : newgrounds.NewgroundsUserExtractor.pattern,
    "#range"   : "76-125",
    "#count"   : 50,
},

{
    "#url"     : "https://www.newgrounds.com/search/conduct/art?terms=tree",
    "#category": ("", "newgrounds", "search"),
    "#class"   : newgrounds.NewgroundsSearchExtractor,
    "#pattern" : newgrounds.NewgroundsImageExtractor.pattern,
    "#range"   : "1-10",
    "#count"   : 10,

    "search_tags": "tree",
},

{
    "#url"     : "https://www.newgrounds.com/search/conduct/movies?terms=tree",
    "#category": ("", "newgrounds", "search"),
    "#class"   : newgrounds.NewgroundsSearchExtractor,
    "#pattern" : r"https://uploads.ungrounded.net(/alternate)?/\d+/\d+",
    "#range"   : "1-10",
    "#count"   : 10,
},

{
    "#url"     : "https://www.newgrounds.com/search/conduct/audio?advanced=1&terms=tree+green+nature&match=tdtu&genre=5&suitabilities=e%2Cm",
    "#category": ("", "newgrounds", "search"),
    "#class"   : newgrounds.NewgroundsSearchExtractor,
},

)
