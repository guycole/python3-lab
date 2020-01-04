#
# Title:gitub1.py
# Description: extract issues from a github repository
# Development Environment:OS X 10.15.2/Python 3.7.4
# Author:Guy Cole (guy at shastrax dot com)
#
import csv
import requests

class Harvester:
    """
    extract issues from a github repository
    """

    def comments(self, buffer):
        """
        parse github issue comments
        :param buffer: raw comments
        :return: list of comments, might be empty
        """
        rows = []
        for candidate in buffer:
            result = {
                'user': candidate['user']['login'],
                'body': candidate['body'],
                'created_at': candidate['created_at'],
                'updated_at': candidate['updated_at'],
            }

            rows.append(result)

        return rows

    def parser(self, buffer, auth_tuple):
        """
        parse github issue
        :param buffer: raw issue
        :param auth_tuple: account and password
        :return: list of issues, might be empty
        """
        rows = []
        for candidate in buffer:
            result = {
                'number': candidate['number'],
                'title': candidate['title'],
                'reporter': candidate['user']['login'],
                'created_at': candidate['created_at'],
                'updated_at': candidate['updated_at'],
                'body': candidate['body'],
            }

            if 'assignee' in candidate and candidate['assignee'] is not None:
                result['assigned'] = candidate['assignee']['login']
            else:
                result['assigned'] = 'nobody'

            comments = []
            comment_population = candidate['comments']
            if comment_population > 0:
                response = requests.get(candidate['comments_url'], auth=auth_tuple)
                if response.status_code == 200:
                    comments = self.comments(response.json())

            result['comments'] = comments

            labels = []
            if 'labels' in candidate:
                for label in candidate['labels']:
                    labels.append(label['name'])

            result['labels'] = labels

            rows.append(result)

        print(f"{len(rows)} issues extracted")
        return rows

    def writer(self, file_name, rows):
        """
        write csv file
        :param file_name: output filename
        :param rows: extracted github issues
        :return: None
        """
        print(f"writing {file_name}")
        with open(file_name, mode='w') as csv_file:
            fieldnames = ['number', 'title', 'reporter', 'assigned', 'created_at', 'updated_at', 'body', 'comments', 'labels']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for row in rows:
                writer.writerow(row)

    def execute(self, user, password, owner, repository):
        """
        drive github issue collection
        :param user:
        :param password:
        :param owner:
        :param repository:
        :return:
        """
        auth_tuple = (user, password)
        header = {"Accept": "application/vnd.github.full+json"}
        url = f"https://api.github.com/repos/{owner}/{repository}/issues"

        response = requests.get(url, auth=auth_tuple, headers=header)
        if response.status_code == 200:
            print(f"successful read from github repository {repository}")
            rows = self.parser(response.json(), auth_tuple)
            self.writer(f"{repository}.csv", rows)
        else:
            print(f"bad status {response.status_code} from github repository {repository}")

print("start")

if __name__ == "__main__":
    print("main")

    harvester = Harvester()
    harvester.execute("account", "password", "owner", "repository")

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***