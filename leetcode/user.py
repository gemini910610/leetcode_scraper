import requests

class User:
    def __init__(self, username):
        self.username = username
        self.url = 'https://leetcode.com/graphql/'
    def __scrape(self, query, params=None, **variables):
        if params is None:
            params = '($username: String!)'
        query = f'''
            query scrape{params}
            {{
                {query}
            }}
        '''
        data = {
            'query': query,
            'variables': variables,
            'operation': 'scrape'
        }
        response = requests.post(self.url, json=data)
        return response.json()['data']
    def __matched_user(self, query, params=None, **variables):
        query = f'''
            matchedUser(username: $username)
            {{
                {query}
            }}
        '''
        data = self.__scrape(query, params, **variables)
        return data['matchedUser']
    def contest_badge(self):
        query = '''
            contestBadge
            {
                name
                expired
                hoverText
                icon
            }
        '''
        data = self.__matched_user(query, username=self.username)
        return data['contestBadge']
    def profile(self):
        query = '''
            profile
            {
                ranking
                userAvatar
                realName
                aboutMe
                school
                websites
                countryName
                company
                jobTitle
                skillTags
                postViewCount
                postViewCountDiff
                reputation
                reputationDiff
                solutionCount
                solutionCountDiff
                categoryDiscussCount
                categoryDiscussCountDiff
                certificationLevel
            }
        '''
        data = self.__matched_user(query, username=self.username)
        return data['profile']
    def language_problem_count(self):
        query = '''
            languageProblemCount
            {
                languageName
                problemsSolved
            }
        '''
        data = self.__matched_user(query, username=self.username)
        return data['languageProblemCount']
    def tag_problem_counts(self):
        query = '''
            tagProblemCounts
            {
                advanced
                {
                    tagName
                    tagSlug
                    problemsSolved
                }
                intermediate
                {
                    tagName
                    tagSlug
                    problemsSolved
                }
                fundamental
                {
                    tagName
                    tagSlug
                    problemsSolved
                }
            }
        '''
        data = self.__matched_user(query, username=self.username)
        return data['tagProblemCounts']
    def submit_stats(self):
        query = '''
            submitStats
            {
                acSubmissionNum
                {
                    difficulty
                    count
                    submissions
                }
                totalSubmissionNum
                {
                    difficulty
                    count
                    submissions
                }
            }
        '''
        data = self.__matched_user(query, username=self.username)
        return data['submitStats']
    def badges(self):
        query = '''
            badges
            {
                id
                name
                shortName
                displayName
                icon
                hoverText
                creationDate
                category
                medal
                {
                    slug
                    config
                    {
                        iconGif
                        iconGifBackground
                    }
                }
            }
        '''
        data = self.__matched_user(query, username=self.username)
        return data['badges']
    def upcoming_badges(self):
        query = '''
            upcomingBadges
            {
                name
                icon
                progress
            }
        '''
        data = self.__matched_user(query, username=self.username)
        return data['upcomingBadges']
    def user_calendar(self, year=None):
        query = '''
            userCalendar(year: $year)
            {
                activeYears
                streak
                totalActiveDays
                dccBadges
                {
                    timestamp
                    badge
                    {
                        name
                        icon
                    }
                }
            }
        '''
        data = self.__matched_user(
            query,
            '($username: String!, $year: Int)',
            username=self.username,
            year=year
        )
        return data['userCalendar']
    def submission_calendar(self):
        query = 'submissionCalendar'
        data = self.__matched_user(query, username=self.username)
        return data['submissionCalendar']
    def active_badge(self):
        query = '''
            activeBadge
            {
                displayName
                icon
            }
        '''
        data = self.__matched_user(query, username=self.username)
        return data['activeBadge']
    def user_url(self):
        query = '''
            githubUrl
            twitterUrl
            linkedinUrl
        '''
        data = self.__matched_user(query, username=self.username)
        return data
    def all_questions_count(self):
        query = '''
            allQuestionsCount
            {
                difficulty
                count
            }
        '''
        data = self.__scrape(query, '')
        return data['allQuestionsCount']
    def user_contest_ranking(self):
        query = '''
            userContestRanking(username: $username)
            {
                attendedContestsCount
                rating
                globalRanking
                totalParticipants
                topPercentage
                badge
                {
                    name
                }
            }
        '''
        data = self.__scrape(query, username=self.username)
        return data['userContestRanking']
    def user_contest_ranking_history(self):
        query = '''
            userContestRankingHistory(username: $username)
            {
                attended
                trendDirection
                problemsSolved
                totalProblems
                finishTimeInSeconds
                rating
                ranking
                contest
                {
                    title
                    startTime
                }
            }
        '''
        data = self.__scrape(query, username=self.username)
        return data['userContestRankingHistory']
    def user_profile_user_question_progress(self):
        query = '''
            userProfileUserQuestionProgressV2(userSlug: $username)
            {
                totalQuestionBeatsPercentage
                numAcceptedQuestions {
                    count
                    difficulty
                }
                numFailedQuestions {
                    count
                    difficulty
                }
                numUntouchedQuestions {
                    count
                    difficulty
                }
                userSessionBeatsPercentage {
                    difficulty
                    percentage
                }
            }
        '''
        data = self.__scrape(query, username=self.username)
        return data['userProfileUserQuestionProgressV2']
    def recent_AC_submission_list(self, limit=15):
        query = '''
            recentAcSubmissionList(username: $username, limit: $limit)
            {
                id
                title
                titleSlug
                timestamp
            }
        '''
        data = self.__scrape(
            query,
            '($username: String!, $limit: Int!)',
            username=self.username,
            limit=limit
        )
        return data['recentAcSubmissionList']
    def created_public_favorite_list(self):
        query = '''
            createdPublicFavoriteList(userSlug: $username)
            {
                hasMore
                totalLength
                favorites
                {
                    slug
                    coverUrl
                    coverEmoji
                    coverBackgroundColor
                    name
                    isPublicFavorite
                    lastQuestionAddedAt
                    hasCurrentQuestion
                    viewCount
                    description
                    questionNumber
                    isDefaultList
                }
            }
        '''
        data = self.__scrape(query, username=self.username)
        return data['createdPublicFavoriteList']
    def can_see_other_submission_history(self):
        query = 'canSeeOtherSubmissionHistory(userSlug: $username)'
        data = self.__scrape(query, username=self.username)
        return data['canSeeOtherSubmissionHistory']
