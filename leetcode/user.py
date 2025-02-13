from .leetcode import LeetCode

class User:
    def __init__(self, username):
        self.username = username
        self.leetcode = LeetCode()
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
        response = self.leetcode.matched_user(query, username=self.username)
        self.leetcode.check_response(response, 'contestBadge')
        return response['contestBadge']
    def profile(self):
        query = '''
            profile
            {
                ranking
                starRating
                userAvatar
                realName
                birthday
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
        response = self.leetcode.matched_user(query, username=self.username)
        self.leetcode.check_response(response, 'profile')
        return response['profile']
    def language_problem_count(self):
        query = '''
            languageProblemCount
            {
                languageName
                problemsSolved
            }
        '''
        response = self.leetcode.matched_user(query, username=self.username)
        self.leetcode.check_response(response, 'languageProblemCount')
        return response['languageProblemCount']
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
        response = self.leetcode.matched_user(query, username=self.username)
        self.leetcode.check_response(response, 'tagProblemCounts')
        return response['tagProblemCounts']
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
        response = self.leetcode.matched_user(query, username=self.username)
        self.leetcode.check_response(response, 'submitStats')
        return response['submitStats']
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
        response = self.leetcode.matched_user(query, username=self.username)
        self.leetcode.check_response(response, 'badges')
        return response['badges']
    def upcoming_badges(self):
        query = '''
            upcomingBadges
            {
                name
                icon
                progress
            }
        '''
        response = self.leetcode.matched_user(query, username=self.username)
        self.leetcode.check_response(response, 'upcomingBadges')
        return response['upcomingBadges']
    def active_badge(self):
        query = '''
            activeBadge
            {
                id
                displayName
                icon
                creationDate
            }
        '''
        response = self.leetcode.matched_user(query, username=self.username)
        self.leetcode.check_response(response, 'activeBadge')
        return response['activeBadge']
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
                submissionCalendar
            }
        '''
        response = self.leetcode.matched_user(query, '($username: String!, $year: Int)', username=self.username, year=year)
        self.leetcode.check_response(response, 'userCalendar')
        return response['userCalendar']
    def submission_calendar(self):
        query = 'submissionCalendar'
        response = self.leetcode.matched_user(query, username=self.username)
        self.leetcode.check_response(response, 'submissionCalendar')
        return response['submissionCalendar']
    def user_url(self):
        query = '''
            githubUrl
            twitterUrl
            linkedinUrl
        '''
        response = self.leetcode.matched_user(query, username=self.username)
        self.leetcode.check_response(response)
        return response
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
        response = self.leetcode.scrape(query, '($username: String!)', username=self.username)
        self.leetcode.check_response(response, 'userContestRanking')
        return response['userContestRanking']
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
        response = self.leetcode.scrape(query, '($username: String!)', username=self.username)
        self.leetcode.check_response(response, 'userContestRankingHistory')
        return response['userContestRankingHistory']
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
        response = self.leetcode.scrape(query, '($username: String!)', username=self.username)
        self.leetcode.check_response(response, 'userProfileUserQuestionProgressV2')
        return response['userProfileUserQuestionProgressV2']
    def recent_submission_list(self, limit=15):
        query = '''
            recentSubmissionList(username: $username, limit: $limit)
            {
                title
                titleSlug
                timestamp
                statusDisplay
                lang
            }
        '''
        response = self.leetcode.scrape(query, '($username: String!, $limit: Int)', username=self.username, limit=limit)
        self.leetcode.check_response(response, 'recentSubmissionList')
        return response['recentSubmissionList']
    def recent_AC_submission_list(self, limit=15):
        query = '''
            recentAcSubmissionList(username: $username, limit: $limit)
            {
                id
                title
                titleSlug
                timestamp
                lang
            }
        '''
        response = self.leetcode.scrape(query, '($username: String!, $limit: Int!)', username=self.username, limit=limit)
        self.leetcode.check_response(response, 'recentAcSubmissionList')
        return response['recentAcSubmissionList']
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
        response = self.leetcode.scrape(query, '($username: String!)', username=self.username)
        self.leetcode.check_response(response, 'createdPublicFavoriteList')
        return response['createdPublicFavoriteList']
    def can_see_other_submission_history(self):
        query = 'canSeeOtherSubmissionHistory(userSlug: $username)'
        response = self.leetcode.scrape(query, '($username: String!)', username=self.username)
        self.leetcode.check_response(response, 'canSeeOtherSubmissionHistory')
        return response['canSeeOtherSubmissionHistory']
