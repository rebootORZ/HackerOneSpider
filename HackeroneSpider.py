
import urllib.request
import requests
import urllib.parse
import json
import simplejson



url = 'https://hackerone.com/graphql'





headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0'
}

values1 = {"operationName":"DirectoryQuery","variables":{"where":{"_and":[{"_or":[{"offers_bounties":{"_eq":"true"}},{"external_program":{"offers_rewards":{"_eq":"true"}}}]},{"_or":[{"submission_state":{"_eq":"open"}},{"submission_state":{"_eq":"api_only"}},{"external_program":{}}]},{"_not":{"external_program":{}}},{"_or":[{"_and":[{"state":{"_neq":"sandboxed"}},{"state":{"_neq":"soft_launched"}}]},{"external_program":{}}]}]},"first":1000000,"secureOrderBy":{"launched_at":{"_direction":"DESC"}}},"query":"query DirectoryQuery($cursor: String, $secureOrderBy: FiltersTeamFilterOrder, $where: FiltersTeamFilterInput) {\n  me {\n    id\n    edit_unclaimed_profiles\n    h1_pentester\n    __typename\n  }\n  teams(first:1000000, after: $cursor, secure_order_by: $secureOrderBy, where: $where) {\n    pageInfo {\n      endCursor\n      hasNextPage\n      __typename\n    }\n    edges {\n      node {\n        id\n        bookmarked\n        ...TeamTableResolvedReports\n        ...TeamTableAvatarAndTitle\n        ...TeamTableLaunchDate\n        ...TeamTableMinimumBounty\n        ...TeamTableAverageBounty\n        ...BookmarkTeam\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment TeamTableResolvedReports on Team {\n  id\n  resolved_report_count\n  __typename\n}\n\nfragment TeamTableAvatarAndTitle on Team {\n  id\n  profile_picture(size: medium)\n  name\n  handle\n  submission_state\n  triage_active\n  publicly_visible_retesting\n  state\n  allows_bounty_splitting\n  external_program {\n    id\n    __typename\n  }\n  ...TeamLinkWithMiniProfile\n  __typename\n}\n\nfragment TeamLinkWithMiniProfile on Team {\n  id\n  handle\n  name\n  __typename\n}\n\nfragment TeamTableLaunchDate on Team {\n  id\n  launched_at\n  __typename\n}\n\nfragment TeamTableMinimumBounty on Team {\n  id\n  currency\n  base_bounty\n  __typename\n}\n\nfragment TeamTableAverageBounty on Team {\n  id\n  currency\n  average_bounty_lower_amount\n  average_bounty_upper_amount\n  __typename\n}\n\nfragment BookmarkTeam on Team {\n  id\n  bookmarked\n  __typename\n}\n"}

data1 = urllib.parse.urlencode(values1).encode('utf-8')

request1 = urllib.request.Request(url, data1, headers)

html1 = urllib.request.urlopen(request1).read().decode('utf-8')

jsondata1 = json.loads(html1)['data']['teams']['edges']
nums1 = len(jsondata1)
for num in range(nums1):
	#print(num)
	company_name = "厂商：" + jsondata1[num-1]['node']['name']
	company_uri = jsondata1[num-1]['node']['handle']
	print(company_name + "  ----  " + company_uri)



	headers = {
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
		"Accept":"*/*",
		"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
		"Accept-Encoding":"gzip, deflate",
		"Referer":"https://hackerone.com/ok?type=team",
		"content-type":"application/json",
		"Origin":"https://hackerone.com",
		"Content-Length":"4516",
		"DNT":"1",
		"Connection":"close",
		"Sec-Fetch-Dest":"empty",
		"Sec-Fetch-Mode":"cors",
		"Sec-Fetch-Site":"same-origin"
		}
	data = "{\"operationName\": \"LayoutDispatcher\", \"variables\": {\"url\": \"" + company_uri + "\"}, \"query\": \"query LayoutDispatcher($url: URI!) {\\n  resource(url: $url) {\\n    ... on ResourceInterface {\\n      url\\n      __typename\\n      ... on Team {\\n        id\\n        type\\n        ...TeamProfileHeaderTeam\\n        __typename\\n      }\\n    }\\n    __typename\\n  }\\n  me {\\n    id\\n    ...TeamProfileHeaderUser\\n    __typename\\n  }\\n}\\n\\nfragment TeamProfileHeaderTeam on Team {\\n  id\\n  name\\n  about\\n  website\\n  handle\\n  only_cleared_hackers\\n  is_team_member\\n  launched_at\\n  offers_bounties\\n  state\\n  offers_thanks\\n  url\\n  triage_active\\n  critical_submissions_enabled\\n  controlled_launch_setting {\\n    id\\n    controlled_launch_team\\n    __typename\\n  }\\n  allows_private_disclosure\\n  allows_bounty_splitting\\n  publicly_visible_retesting\\n  policy_setting {\\n    id\\n    i_can_subscribe_to_policy_changes\\n    __typename\\n  }\\n  submission_state\\n  i_can_view_program_info\\n  i_can_view_hacktivity\\n  i_can_view_pentests\\n  i_can_view_checklist_checks\\n  child_program_directory_enabled\\n  resolved_report_count\\n  profile_picture(size: large)\\n  cover_color\\n  cover_photo_url\\n  has_cover_photo\\n  has_cover_video\\n  twitter_handle\\n  checklist {\\n    id\\n    checklist_checks {\\n      total_count\\n      __typename\\n    }\\n    __typename\\n  }\\n  structured_scopes {\\n    edges {\\n      node {\\n        id\\n        asset_identifier\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n  child_teams {\\n    total_count\\n    edges {\\n      node {\\n        id\\n        name\\n        handle\\n        offers_bounties\\n        profile_picture(size: medium)\\n        structured_scopes {\\n          edges {\\n            node {\\n              id\\n              asset_identifier\\n              __typename\\n            }\\n            __typename\\n          }\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n  posts {\\n    total_count\\n    __typename\\n  }\\n  external_program {\\n    id\\n    __typename\\n  }\\n  assets_in_scope: structured_scopes(archived: false, eligible_for_submission: true) {\\n    total_count\\n    __typename\\n  }\\n  ...TeamTableAverageBounty\\n  ...TeamTableResolvedReports\\n  ...TeamCTATeam\\n  ...TeamContentBanner\\n  ...TeamNoticeBanner\\n  ...BookmarkTeam\\n  __typename\\n}\\n\\nfragment TeamTableAverageBounty on Team {\\n  id\\n  currency\\n  average_bounty_lower_amount\\n  average_bounty_upper_amount\\n  __typename\\n}\\n\\nfragment TeamTableResolvedReports on Team {\\n  id\\n  resolved_report_count\\n  __typename\\n}\\n\\nfragment TeamCTATeam on Team {\\n  id\\n  abuse\\n  allows_private_disclosure\\n  allows_disclosure_assistance\\n  allows_bounty_splitting\\n  publicly_visible_retesting\\n  handle\\n  external_url\\n  submission_state\\n  policy_setting {\\n    id\\n    __typename\\n  }\\n  i_reached_abuse_limit\\n  i_can_view_private\\n  i_can_view_private_program_application_requirement\\n  i_can_create_report\\n  i_can_view_hacktivity\\n  i_can_edit_program_profile\\n  facebook_team\\n  settings_link\\n  external_program {\\n    id\\n    disclosure_email\\n    disclosure_url\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment TeamContentBanner on Team {\\n  id\\n  name\\n  handle\\n  critical_submissions_enabled\\n  submission_state\\n  __typename\\n}\\n\\nfragment TeamNoticeBanner on Team {\\n  id\\n  handle\\n  state\\n  offers_bounties\\n  ...DemoTeamNoticeBanner\\n  ...SoftLaunchedTeamNoticeBanner\\n  __typename\\n}\\n\\nfragment DemoTeamNoticeBanner on Team {\\n  id\\n  allowed_to_use_saml_in_sandbox\\n  handle\\n  has_avatar\\n  has_payment_method\\n  policy_setting {\\n    id\\n    has_policy\\n    __typename\\n  }\\n  controlled_launch_setting {\\n    id\\n    controlled_launch_team\\n    __typename\\n  }\\n  launch_link\\n  offers_bounties\\n  review_requested_at\\n  review_rejected_at\\n  state\\n  team_member_groups {\\n    id\\n    permissions\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment SoftLaunchedTeamNoticeBanner on Team {\\n  id\\n  name\\n  i_can_view_invite_hackers\\n  launch_link\\n  i_am_a_whitelisted_reporter\\n  __typename\\n}\\n\\nfragment BookmarkTeam on Team {\\n  id\\n  bookmarked\\n  __typename\\n}\\n\\nfragment TeamProfileHeaderUser on User {\\n  id\\n  has_active_ban\\n  ...TeamCTAMe\\n  ...BanNoticeModal\\n  __typename\\n}\\n\\nfragment TeamCTAMe on User {\\n  id\\n  has_active_ban\\n  __typename\\n}\\n\\nfragment BanNoticeModal on User {\\n  id\\n  active_ban {\\n    id\\n    starts_at\\n    ends_at\\n    duration_in_days\\n    __typename\\n  }\\n  __typename\\n}\\n\"}"


	request2 = requests.post(url, headers=headers, data=data)

	jsondata2 = request2.json()['data']['resource']['structured_scopes']['edges']


	nums2 = len(jsondata2)
	if(nums2 > 0):
		for num in range(nums2):
			scope = jsondata2[num-1]['node']['asset_identifier']
			print(scope)
