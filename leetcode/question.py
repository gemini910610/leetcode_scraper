import requests

class Question:
    def __init__(self):
        self.url = 'https://leetcode.com/graphql/'
    def __scrape(self, query, params=None, **variables):
        if params is None:
            params = ''
        query = f'''
            query scrape{params}
            {{
                {query}
            }}
        '''
        data = {
            'query': query,
            'variables': variables
        }
        response = requests.post(self.url, json=data)
        return response.json()['data']
    def all_questions_count(self):
        query = '''
            allQuestionsCount
            {
                difficulty
                count
            }
        '''
        data = self.__scrape(query)
        return data['allQuestionsCount']
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
        data = self.__scrape(query, '($titleSlug: String!)', titleSlug=titleSlug)
        return data['question']
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
        data = self.__scrape(query)
        return data['activeDailyCodingChallengeQuestion']
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
        data = self.__scrape(query, '($year: Int!, $month: Int!)', year=year, month=month)
        return data['dailyCodingChallengeV2']
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
        data = self.__scrape(query, '($year: Int!, $month: Int!)', year=year, month=month)
        return data['dailyChallengeMedal']
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
        data = self.__scrape(query, '($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput)', categorySlug=categorySlug, limit=limit, skip=skip, filters=filters)
        return data['questionList']
