import os
import sqlite3
import shutil


class Query(object):
    query = (
        "SELECT DISTINCT urls.url, "
        "urls.visit_count FROM urls, "
        "visits WHERE urls.id = visits.url "
        "ORDER BY urls.visit_count desc;"
    )



    def all(self):
        return self.execute(self.query)

    def execute(self, query=query):

        try:
            self.scrapper.cursor.execute(query)
        except Exception as err:
            raise Exception('Error: ' + repr(err))
        else:
            return self.scrapper.cursor.fetchall()

    def tables(self):
        return self.execute(
            query="SELECT name FROM sqlite_master WHERE type='table';")

    def get_num_users(self):
        return len(self.execute("SELECT * FROM queue;"))


class ChromeHistoryScrapper(object):
    query = Query()

    def __init__(self,
                 history_path='~/.config/google-chrome/Default/',
                 term=None,
                 file_name='History.sqlite',
                 export_path='./data'):
        self.history_path = os.path.expanduser(history_path)
        self.term = term
        self.file_name = file_name
        self.export_path = os.path.expanduser(export_path)
        if not os.path.exists(self.export_path):
            os.makedirs(self.export_path)
        self.history_files = os.listdir(self.history_path)
        self.file_export_path = os.path.join(self.export_path, self.file_name)
        self.history_db = os.path.join(self.history_path, 'History')

        shutil.copy2(self.history_db, self.file_export_path)

        self.connection = sqlite3.connect(self.file_export_path, timeout=10)
        self.connection.text_factory = str
        self.cursor = self.connection.cursor()
        self.query.scrapper = self


def main():
    print(ChromeHistoryScrapper.query.all())


if __name__ == '__main__':
    main()
