// Найдите трек с наивысшими показателями  Danceability и Energy.
db.Spotify_Youtube.aggregate([
    {
        $sort:
            {
                Danceability: -1,
                Energy: -1
            }
    },
    {
        $limit:
            1
    },
    {
        $project:
            {
                Track: 1,
                Artist: 1,
                _id: 0
            }
    }
])
// Ответ:
// {
//   "Artist": "Timbaland",
//   "Track": "Give It To Me"
// }

// У какого трека (но не compilation) самая большая длительность?
db.Spotify_Youtube.aggregate([
    {
        $match: {
            Album_type: {
                $ne: "compilation"
            }
        }
    },
    {
        $sort:
            {
                Duration_ms: -1
            }
    },
    {
        $limit:
            1
    },
    {
        $project:
            {
                Artist: 1,
                Track: 1,
                _id: 0
            }
    }
])
// Ответ:
// {
//   "Artist": "Ocean Waves For Sleep",
//   "Track": "Ocean Waves for Sleep"
// }

// В каком одном альбоме самое большее количество треков?
db.Spotify_Youtube.aggregate([
    {
        $group:
            {
                _id: "$Album",
                song_count: {
                    $sum: 1
                }
            }
    },
    {
        $sort:
            {
                song_count: -1
            }
    },
    {
        $limit:
            1
    }
])
// Ответ:
// {
//   "_id": "Greatest Hits",
//   "song_count": 30
// }

// Сколько просмотров видео на youtube у трека с самым высоким количеством прослушиваний на spotify (Stream)?
db.Spotify_Youtube.aggregate([
    {
        $project:
            {
                Views: 1,
                Stream: 1,
                _id: 0
            }
    },
    {
        $sort:
            {
                Stream: -1
            }
    },
    {
        $project:
            {
                Views: 1
            }
    },
    {
        $limit:
            1
    }
])
// Ответ: 674164500

// Экспортируйте 20 самых популярных (прослушивания или просмотры) треков по версиям youtube и spotify и импортируйте
// в базу ich_edit их с именами top20youtube и top20spotify, и добавьте им свои имена для уникальности.
db.getCollection('Spotify_Youtube').aggregate(
  [{ $sort: { Views: -1 } }, { $limit: 20 }],
  { maxTimeMS: 60000, allowDiskUse: true }
);

db.getCollection('Spotify_Youtube').aggregate(
  [{ $sort: { Stream: -1 } }, { $limit: 20 }],
  { maxTimeMS: 60000, allowDiskUse: true }
);
// так как на том же сервере, где лежит коллекция Spotify_Youtube у нас нету прав на запись в базу ich_edit -
// экспортировал результат аггрегации в виде json и потом уже импортировал на другом сервере