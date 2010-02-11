import yql

class MemeRepository(object):
    def __init__(self):
        self.yql = yql.Public()

    def _yql_query(self, query):
        posts = []
        result = self.yql.execute(query)
        for row in result.rows:
            posts.append(Post(row))
        return posts

    def popular(self, locale):
        query = 'SELECT * FROM meme.popular WHERE locale="%s"' % locale;
        return self._yql_query(query)
        
    

# SELECT * FROM meme.following WHERE owner_guid in (select guid from meme.info where name = "guilherme_chapiewski")
        
class Meme(object):
    def __init__(self, data):
        self.guid = data['guid']
        self.name = data['name']
        self.title = data['title']
        self.description = data['description']
        self.url = data['url']
        self.avatar_url = data['avatar_url']
        self.language = data['language']
        self.follower_count = data['follower']
        
    def __repr__(self):
        return u'Meme[guid=%s, name=%s]' % (self.guid, self.name)

class Post(object):
    def __init__(self, data):
        self.guid = data['guid'] #meme id
        self.pubid = data['pubid'] #post id
        self.type = data['type']
        self.content = data['content']
        self.caption = data['caption']
        self.comment = data['comment']
        self.url = data['url']
        self.timestamp = data['timestamp']
        self.origin_guid = data['origin_guid'] #if empty then not a repost
        self.origin_pubid = data['origin_pubid'] #if empty then not a repost
        self.via_guid = data['via_guid'] #if empty then not a repost
        self.repost_count = data['repost_count']
    
    def __repr__(self):
        return u'Post[guid=%s, pubid=%s, type=%s]' % (self.guid, self.pubid, self.type)
    
    def __unicode__(self):
        return u'Post[comment=%s, via_guid=%s, url=%s, timestamp=%s, \
                pubid=%s, repost_count=%s, origin_guid=%s, content=%s, \
                caption=%s, origin_pubid=%s, guid=%s, type=%s]'% (
                self.comment, self.via_guid, self.url, self.timestamp, 
                self.pubid, self.repost_count, self.origin_guid, self.content, 
                self.caption, self.origin_pubid, self.guid, self.type)