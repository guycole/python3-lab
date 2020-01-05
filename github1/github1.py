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


    def repo(self, owner, auth_tuple):
        """
        return a list of repositories
        :param owner:
        :param auth_tuple:
        :return:
        """
        results = []
        url = f"https://api.github.com/orgs/{owner}/repos?type=all"

        response = requests.get(url, auth=auth_tuple)
        print(response.content)
        if response.status_code == 200:
            for row in response.json():
                results.append(row['name'])

        # NOTE: does not return all the expected repositories (only 30 for scoop, vs 200 promised
        return results

    def comment(self, buffer):
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
                    comments = self.comment(response.json())

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
        print(f"writing {file_name} with row population {len(rows)}")
        with open(file_name, mode='w') as csv_file:
            fieldnames = ['number', 'title', 'reporter', 'assigned', 'created_at', 'updated_at', 'body', 'comments', 'labels']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for row in rows:
                writer.writerow(row)


    def paginator(self, headers):
        """
        discover if this repository paginates for issues
        :param headers: raw response header
        :return: tuple in the form (next_page, max_page, base_url)
        """
        base_url = ''
        min_ndx = 0
        max_ndx = 0

        if 'Link' in headers:
            link = headers['Link']
            #
            # https://developer.github.com/v3/guides/traversing-with-pagination/
            #
            # if link is present, there is pagination and results look like this
            # <https://api.github.com/repositories/33013398/issues?per_page=100&page=2>; rel="next",
            # <https://api.github.com/repositories/33013398/issues?per_page=100&page=3>; rel="last"
            #
            # Discover 'base' URL and min, max additional pages
            #
            split1 = link.split(';')
            next_page = split1[0]
            last_page = split1[1]

            ndx1 = next_page.rfind('=')
            ndx2 = next_page.rfind('>')
            base_url = next_page[1:ndx1+1]
            # base_url = https://api.github.com/repositories/33013398/issues?per_page=100&page=
            min_ndx = next_page[ndx1+1:ndx2]

            ndx1 = last_page.rfind('=')
            ndx2 = last_page.rfind('>')
            max_ndx = last_page[ndx1+1:ndx2]

        return (int(min_ndx), int(max_ndx), base_url)


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

        rows = []
        print("page count:1")

        # initial remote read
        url = f"https://api.github.com/repos/{owner}/{repository}/issues?per_page=100"
        response = requests.get(url, auth=auth_tuple, headers=header)
        if response.status_code == 200:
            print(f"successful read from github repository {repository}")
            rows += self.parser(response.json(), auth_tuple)

            # might paginate and require additional visits
            page_tuple = self.paginator(response.headers)
            if len(page_tuple[2]) > 0:
                for page_ndx in range(page_tuple[0], 1+page_tuple[1]):
                    print(f"page count:{page_ndx} of {page_tuple[1]}")
                    url = f"{page_tuple[2]}{page_ndx}"

                    response = requests.get(url, auth=auth_tuple, headers=header)
                    if response.status_code == 200:
                        print(f"successful read from github repository {repository}")
                        rows += self.parser(response.json(), auth_tuple)
                    else:
                        print(f"bad status {response.status_code} from github repository {repository}")
        else:
            print(f"bad status {response.status_code} from github repository {repository}")

        if len(rows) > 0:
            self.writer(f"{repository}.csv", rows)
        else:
            print("skipping output file")


print("start")

if __name__ == "__main__":
    print("main")

    harvester = Harvester()
    harvester.execute("account", "password", "owner", "repository")

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***