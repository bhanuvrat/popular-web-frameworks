
import requests
import yaml
import json
import os

relevant_keys = [
    'homepage', 'description', 'html_url', 'size', 'stargazers_count',
    'forks_count', 'open_issues_count', 'name', 'language'
]


def main():
    final = []
    headers = {'Authorization': 'Token %s' % os.environ.get('GH_TOKEN')}

    with open('frameworks.yml') as f:
        frameworks = yaml.load(f)

    for framework in frameworks:
        r = requests.get(
            url="https://api.github.com/repos/%s" % framework['repo_name'],
            headers=headers)
        response_dict = r.json()
        relevant_subset = {k: response_dict.get(k) for k in relevant_keys}
        final.append(relevant_subset)

    data = json.dumps({'files': {'frameworks.json': {
        'content': json.dumps({'data': final}, sort_keys=True, indent=4)
    }}})

    requests.patch(
        url="https://api.github.com/gists/dc1e1ec6e3a17437a150",
        headers=headers, data=data
    )

    # with open('data.json', 'w') as f:
    #     json.dump({'data': final}, f)


if __name__ == '__main__':
    main()
