from .leetcode import LeetCode

class Question:
    def __init__(self):
        self.leetcode = LeetCode()
    def all_questions_count(self):
        query = '''
            allQuestionsCount
            {
                difficulty
                count
            }
        '''
        response = self.leetcode.scrape(query)
        self.leetcode.check_response(response, 'allQuestionsCount')
        return response['allQuestionsCount']
    def question(self, titleSlug):
        query = '''
            question(titleSlug: $titleSlug)
            {
                questionId
                questionFrontendId
                boundTopicId
                title
                titleSlug
                content
                translatedTitle
                translatedContent
                isPaidOnly
                difficulty
                likes
                dislikes
                isLiked
                similarQuestions
                exampleTestcases
                contributors
                {
                    username
                    profileUrl
                    avatarUrl
                }
                topicTags
                {
                    name
                    slug
                    translatedName
                }
                companyTagStats
                codeSnippets
                {
                    lang
                    langSlug
                    code
                }
                stats
                hints
                solution
                {
                    id
                    title
                    content
                    contentTypeId
                    canSeeDetail
                    paidOnly
                    hasVideoSolution
                    paidOnlyVideo
                    rating
                    {
                        count
                        average
                        userRating
                        {
                            score
                        }
                    }
                    topic
                    {
                        id
                        commentCount
                        topLevelCommentCount
                        viewCount
                        subscribed
                        solutionTags
                        {
                            name
                            slug
                        }
                        post
                        {
                            id
                            status
                            creationDate
                            author
                            {
                                username
                                isActive
                                profile
                                {
                                    userAvatar
                                    reputation
                                }
                            }
                        }
                    }
                }
                status
                sampleTestCase
                metaData
                judgerAvailable
                judgeType
                mysqlSchemas
                enableRunCode
                enableTestMode
                enableDebugger
                envInfo
                libraryUrl
                adminUrl
                challengeQuestion
                {
                    id
                    date
                    incompleteChallengeCount
                    streakCount
                    type
                }
                note
            }
        '''
        response = self.leetcode.scrape(query, '($titleSlug: String!)', titleSlug=titleSlug)
        self.leetcode.check_response(response, 'question')
        return response['question']
    def active_daily_coding_challenge_question(self):
        query = '''
            activeDailyCodingChallengeQuestion
            {
                date
                userStatus
                link
                question
                {
                    questionId
                    boundTopicId
                    titleSlug
                    title
                    translatedTitle
                    acRate
                    difficulty
                    freqBar
                    questionFrontendId
                    isFavor
                    isPaidOnly
                    status
                    hasVideoSolution
                    hasSolution
                    topicTags
                    {
                        name
                        id
                        slug
                        translatedName
                    }
                    content
                    translatedContent
                    similarQuestions
                    exampleTestcases
                    likes
                    dislikes
                    isLiked
                    contributors
                    {
                        username
                        profileUrl
                        avatarUrl
                    }
                    companyTagStats
                    codeSnippets
                    {
                        lang
                        langSlug
                        code
                    }
                    stats
                    hints
                    solution
                    {
                        id
                        canSeeDetail
                        paidOnly
                        hasVideoSolution
                        paidOnlyVideo
                    }
                    status
                    sampleTestCase
                    metaData
                    judgerAvailable
                    judgeType
                    mysqlSchemas
                    enableRunCode
                    enableTestMode
                    enableDebugger
                    envInfo
                    libraryUrl
                    adminUrl
                    challengeQuestion
                    {
                        id
                        date
                        incompleteChallengeCount
                        streakCount
                        type
                    }
                    note
                }
            }
        '''
        response = self.leetcode.scrape(query)
        self.leetcode.check_response(response, 'activeDailyCodingChallengeQuestion')
        return response['activeDailyCodingChallengeQuestion']
    def daily_coding_challenge(self, year, month):
        query = '''
            dailyCodingChallengeV2(year: $year, month: $month)
            {
                challenges
                {
                    date
                    userStatus
                    link
                    question
                    {
                        questionFrontendId
                        title
                        titleSlug
                    }
                }
            }
        '''
        response = self.leetcode.scrape(query, '($year: Int!, $month: Int!)', year=year, month=month)
        self.leetcode.check_response(response, 'dailyCodingChallengeV2')
        return response['dailyCodingChallengeV2']
    def daily_challenge_medal(self, year, month):
        query = '''
            dailyChallengeMedal(year: $year, month: $month)
            {
                name
                config
                {
                    icon
                }
            }
        '''
        response = self.leetcode.scrape(query, '($year: Int!, $month: Int!)', year=year, month=month)
        self.leetcode.check_response(response, 'dailyChallengeMedal')
        return response['dailyChallengeMedal']
    def question_list(self, categorySlug='all-code-essentials', limit=50, skip=0, filters=None):
        if filters is None:
            filters = {}
            # orderBy: FRONTEND_ID, AC_RATE, DIFFICULTY
            # sortOrder: DESCENDING, ASCENDING
            # difficulty: EASY, MEDIUM, HARD
            # tags: [array]
            # searchKeywords: 'two sum'
        query = '''
            questionList(categorySlug: $categorySlug, limit: $limit, skip: $skip, filters: $filters)
            {
                totalNum
                questions: data
                {
                    acRate
                    difficulty
                    freqBar
                    questionFrontendId
                    isFavor
                    isPaidOnly
                    status
                    title
                    titleSlug
                    topicTags
                    {
                        name
                        id
                        slug
                    }
                    hasSolution
                    hasVideoSolution
                    content
                    similarQuestions
                    exampleTestcases
                }
            }
        '''
        response = self.leetcode.scrape(query, '($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput)', categorySlug=categorySlug, limit=limit, skip=skip, filters=filters)
        self.leetcode.check_response(response, 'questionList')
        return response['questionList']
