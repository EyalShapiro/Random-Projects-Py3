from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import random


from .utils.func import create_sent_build_item, encode_image_to_base64, is_valid_header


def http_error_response():
    return HttpResponseForbidden(
        {"error": "method not allowed or invalid header value", "status": 403, "message": "Forbidden"}
    )


@csrf_exempt
def home(request):
    if request.method == "GET" and is_valid_header(request):
        return JsonResponse({"you": "fat"})
    else:
        return http_error_response()


def get_listen_qsts(request):
    if request.method == "GET" and is_valid_header(request):
        listening_item_list = [
            {"sentence": "The boy is biting the dog's tail"},
            {"sentence": "My cat tried to teach our goldfish how to play chess"},
            {"sentence": "Last night I dreamt my teddy bear went to school to learn karate"},
            {"sentence": "A group of frogs formed a band and played jazz at the pond"},
            {"sentence": "I saw a squirrel taking selfies with a tiny camera in the garden"},
            {"sentence": "Our vacuum cleaner suddenly started singing opera during cleaning"},
        ]

        # Shuffle the entire list
        random.shuffle(listening_item_list)

        # Retrieve the number of questions to return from the query parameter
        num_of_questions = request.GET.get("numOfQuestions", default=len(listening_item_list))
        try:
            num_of_questions = int(num_of_questions)
        except ValueError:
            return JsonResponse({"error": "Invalid number format"}, status=400)

        # Return only the requested number of questions
        limited_list = listening_item_list[:num_of_questions]

        return JsonResponse(limited_list, safe=False)

    else:
        return http_error_response()


def get_sent_build_qsts(request):
    if request.method == "GET" and is_valid_header(request):
        sent_build_item_list = [
            create_sent_build_item(
                "אני לומד למבחנים שלי לאחרונה",
                ["I have been studying for my exams recently"],
            ),
            create_sent_build_item("הגבעה הזו לא גבוהה", ["This hill is not tall"]),
            create_sent_build_item("זה כלב גדול", ["This is a big dog"]),
            create_sent_build_item("הילד אוכל תפוח", ["The child is eating an apple"]),
            create_sent_build_item("אני לומד למבחנים שלי לאחרונה", ["I have been studying for my exams recently"]),
            create_sent_build_item(
                "השפעת שינוי האקלים הופכת להיות יותר ברורה",
                [
                    "The impact of climate change is becoming more evident",
                    "The climate change impact is becoming more evident",
                ],
            ),
            create_sent_build_item(
                "קריאה מרחיבה את הדעת ומעשירה את אוצר המילים",
                ["Reading broadens the mind and enriches the vocabulary"],
            ),
            create_sent_build_item(
                "השתתפות בספורט קבוצתי בונה אופי ומיומנויות ניהול",
                ["Participating in team sports builds character and leadership skills"],
            ),
            create_sent_build_item(
                "עלינו להתמודד עם הדאגות הגוברות בנוגע לאבטחת מידע",
                ["We need to address the growing concerns about cyber security"],
            ),
            create_sent_build_item(
                "לימודי ההיסטוריה עוזרים לנו להבין את ההווה",
                ["The study of history helps us understand the present"],
            ),
            create_sent_build_item(
                "טכנולוגיה מתקדמת תמשיך להביא למהפכה בחיינו",
                ["Advanced technology will continue to revolutionize our lives"],
            ),
            create_sent_build_item(
                "שינויי אקלים הם בעיה עולמית חשובה",
                ["Climate change is a significant global issue"],
            ),
            create_sent_build_item(
                "ספרות לעיתים קרובות משקפת את החברה שבה נכתבה",
                ["Literature often reflects the society it was written in"],
            ),
            create_sent_build_item(
                "התקדמויות מדעיות שינו את חיינו באופן דרמטי",
                [
                    "Scientific advancements have dramatically changed our lives",
                    "Scientific advancements have changed our lives dramatically",
                ],
            ),
            create_sent_build_item(
                "הבנת תרבויות שונות מקדמת סובלנות",
                ["Understanding different cultures promotes tolerance"],
            ),
            create_sent_build_item(
                "מיומנויות תקשורת יעילות הן חיוניות להצלחה",
                ["Effective communication skills are essential for success"],
            ),
            create_sent_build_item(
                "השפעת הטכנולוגיה על החברה עמוקה",
                ["The impact of technology on society is profound"],
            ),
            create_sent_build_item(
                "שימור הסביבה חיוני לדורות הבאים",
                ["Environmental conservation is crucial for future generations"],
            ),
            create_sent_build_item(
                "חקר החלל תמיד עניין את בני האדם",
                ["Exploring space has always fascinated humans"],
            ),
            create_sent_build_item(
                "קריאה מרחיבה את אופקינו ונקודות המבט שלנו",
                ["Reading broadens our horizons and perspectives"],
            ),
            create_sent_build_item(
                "הדמוקרטיה מתבססת על עקרון השוויון",
                ["Democracy relies on the principle of equality"],
            ),
            create_sent_build_item(
                "תזונה משחקת תפקיד קריטי בשמירה על הבריאות",
                ["Nutrition plays a crucial role in maintaining health"],
            ),
            create_sent_build_item(
                "ביטוי אומנותי הוא השתקפות של נפש האדם",
                ["Artistic expression is a reflection of the human spirit"],
            ),
            create_sent_build_item(
                "שיקולים אתיים הם חיוניים במחקר מדעי",
                ["Ethical considerations are vital in scientific research"],
            ),
            create_sent_build_item(
                "לימוד שפה שנייה מביא עמו הרבה יתרונות קוגניטיביים",
                ["Learning a second language has many cognitive benefits"],
            ),
            create_sent_build_item(
                "התקשורת משחקת תפקיד חשוב בעיצוב דעת הקהל",
                ["The media plays a significant role in shaping public opinion"],
            ),
            create_sent_build_item(
                "מדיניות כלכלית יכולה להשפיע משמעותית על איכות החיים",
                ["Economic policies can significantly impact the quality of life"],
            ),
            create_sent_build_item(
                "חקר פילוסופיות שונות מרחיב את הבנתנו של העולם",
                ["Exploring different philosophies broadens our understanding of the world"],
            ),
            create_sent_build_item(
                "שיתוף פעולה בינלאומי הוא המפתח לפתרון אתגרים עולמיים",
                ["International cooperation is key to solving global challenges"],
            ),
            create_sent_build_item(
                "פעילות גופנית חשובה גם לבריאות הנפשית וגם לגופנית",
                ["Physical exercise is important for both mental and physical health"],
            ),
        ]

        # Shuffle the entire list
        random.shuffle(sent_build_item_list)
        num_of_questions = None

        # Retrieve the number of questions to return from the query parameter
        try:
            num_of_questions = request.GET.get("numOfQuestions", default=len(sent_build_item_list))
            num_of_questions = int(num_of_questions)
        except ValueError:
            return JsonResponse({"error": "Invalid number format"}, status=400)

        # Return only the requested number of questions
        limited_list = sent_build_item_list[:num_of_questions]

        return JsonResponse(limited_list, safe=False)

    else:
        return http_error_response()


def get_unseen_qsts(request):
    if request.method == "GET" and is_valid_header(request):
        unseen_item_list = [
            {
                "title": "The Forgotten Diary",
                "introImageBase64": encode_image_to_base64("images/Sarah_attic.jpg"),
                "text": "In the dusty attic, Sarah discovered an old diary belonging to her great-grandmother. The entries revealed a young woman's dreams and struggles during the 1920s. Intrigued, Sarah spent hours reading about forgotten love stories and untold family secrets. The diary not only unveiled her ancestor's life but also inspired Sarah to start her own journal.",
                "unseenQuestions": [
                    {
                        "question": "What was dusty?",
                        "correctAnswer": "The attic",
                        "wrongAnswers": ["The young woman", "Sarah", "The diary"],
                        "quote": "In the dusty attic",
                    },
                    {
                        "question": "What was the diary about",
                        "correctAnswer": "The dreams and struggles of a young woman",
                        "wrongAnswers": [
                            "Dusty attics",
                            "The 1920s",
                            "How Sarah started her journal",
                        ],
                        "quote": "The entries revealed a young woman's dreams and struggles",
                    },
                    {
                        "question": "How did the revelation affect Sarah?",
                        "correctAnswer": "She started her own journal",
                        "wrongAnswers": [
                            "She became a young woman",
                            "She met her ancestors",
                            "She loved the stories",
                        ],
                        "quote": "also inspired Sarah to start her own journal",
                    },
                ],
            },
            {
                "title": "Stargazing Adventure",
                "introImageBase64": encode_image_to_base64("images/Stargazing_adventure.jpg"),
                "text": "On a clear night, Alex and his friends decided to watch the stars from the hilltop near their town. As they gazed up, they spotted a faint, moving light crossing the sky. Fascinated, they realized it was a satellite. Alex felt a deep connection with the vast universe and pondered humanity's role in it, sparking his interest in astronomy.",
                "unseenQuestions": [
                    {
                        "question": "Where did Alex and his friends go to watch the stars?",
                        "correctAnswer": "The hilltop near their town",
                        "wrongAnswers": [
                            "The town center",
                            "A nearby forest",
                            "Their backyard",
                        ],
                        "quote": "On a clear night, Alex and his friends decided to watch the stars from the hilltop near their town",
                    },
                    {
                        "question": "What did they spot in the sky?",
                        "correctAnswer": "A satellite",
                        "wrongAnswers": [
                            "A shooting star",
                            "A comet",
                            "An airplane",
                        ],
                        "quote": "As they gazed up, they spotted a faint, moving light crossing the sky. Fascinated, they realized it was a satellite",
                    },
                    {
                        "question": "What was the outcome of their stargazing?",
                        "correctAnswer": "Alex developed an interest in astronomy",
                        "wrongAnswers": [
                            "They became frightened",
                            "They discovered a new star",
                            "Alex felt disconnected from the universe",
                        ],
                        "quote": "Alex felt a deep connection with the vast universe and pondered humanity's role in it, sparking his interest in astronomy",
                    },
                ],
            },
            {
                "title": "The Final Shot",
                "introImageBase64": encode_image_to_base64("images/Maya_basketball.jpg"),
                "text": "The championship game was down to the last play, and Maya had the ball. Her team was trailing by two points. With determination, she dodged past defenders and took the shot just as the buzzer sounded. The ball swooshed through the net, winning the game. Maya's teammates rushed to celebrate, proving that perseverance and teamwork can lead to triumph.",
                "unseenQuestions": [
                    {
                        "question": "What was the situation when Maya had the ball?",
                        "correctAnswer": "Her team was trailing by two points",
                        "wrongAnswers": [
                            "Her team was leading",
                            "The game was tied",
                            "It was the beginning of the game",
                        ],
                        "quote": "Her team was trailing by two points",
                    },
                    {
                        "question": "What did Maya do as the buzzer sounded?",
                        "correctAnswer": "She took a shot",
                        "wrongAnswers": [
                            "She passed the ball",
                            "She scored a penalty",
                            "She called a timeout",
                        ],
                        "quote": "With determination, she dodged past defenders and took the shot just as the buzzer sounded",
                    },
                    {
                        "question": "What was the result of Maya's action?",
                        "correctAnswer": "Her team won the game",
                        "wrongAnswers": [
                            "Her team lost the game",
                            "The game went into overtime",
                            "She missed the shot",
                        ],
                        "quote": "The ball swooshed through the net, winning the game",
                    },
                ],
            },
            {
                "title": "The Mysterious Gardener",
                "introImageBase64": encode_image_to_base64("images/Tim_garden.jpg"),
                "text": "Every morning, the elderly Mrs. Jensen found her garden weeded and the flowers watered. She wondered who the mysterious helper could be. One day, she caught a glimpse of her neighbor's son, Tim, sneaking away from her yard. Grateful, she baked him a pie, leaving it on his doorstep with a note of thanks, reminding them both of the joy of kindness.",
                "unseenQuestions": [
                    {
                        "question": "What did Mrs. Jensen find in her garden every morning?",
                        "correctAnswer": "Her garden weeded and the flowers watered",
                        "wrongAnswers": ["A new plant", "Damaged flowers", "A garden gnome"],
                        "quote": "Every morning, the elderly Mrs. Jensen found her garden weeded and the flowers watered",
                    },
                    {
                        "question": "Who was the mysterious helper in Mrs. Jensen's garden?",
                        "correctAnswer": "Her neighbor's son, Tim",
                        "wrongAnswers": ["A gardener", "Her grandson", "A friend"],
                        "quote": "One day, she caught a glimpse of her neighbor's son, Tim, sneaking away from her yard",
                    },
                    {
                        "question": "How did Mrs. Jensen show her gratitude?",
                        "correctAnswer": "She baked a pie for Tim",
                        "wrongAnswers": [
                            "She gave him money",
                            "She planted a tree in his honor",
                            "She wrote a letter to the newspaper",
                        ],
                        "quote": "Grateful, she baked him a pie, leaving it on his doorstep with a note of thanks",
                    },
                ],
            },
            {
                "title": "The Subway Violinist",
                "introImageBase64": encode_image_to_base64("images/Julia_violin.jpg"),
                "text": "In the bustling city, Julia often played her violin at the subway station. One day, a famous music producer heard her playing an original composition and was captivated. He approached Julia with an offer to record her music. This chance encounter opened the door to a world of opportunities, teaching her that talent can be discovered in the most unexpected places.",
                "unseenQuestions": [
                    {
                        "question": "Where did Julia usually play her violin?",
                        "correctAnswer": "At the subway station",
                        "wrongAnswers": ["In a concert hall", "At a music school", "On a street corner"],
                        "quote": "In the bustling city, Julia often played her violin at the subway station",
                    },
                    {
                        "question": "Who discovered Julia’s talent?",
                        "correctAnswer": "A famous music producer",
                        "wrongAnswers": ["A subway passenger", "A music teacher", "A radio host"],
                        "quote": "One day, a famous music producer heard her playing an original composition and was captivated",
                    },
                    {
                        "question": "What opportunity arose from this encounter?",
                        "correctAnswer": "An offer to record her music",
                        "wrongAnswers": [
                            "A scholarship to a music school",
                            "A chance to play in an orchestra",
                            "A television interview",
                        ],
                        "quote": "He approached Julia with an offer to record her music",
                    },
                ],
            },
        ]

        # Shuffle the entire list
        random.shuffle(unseen_item_list)

        # Retrieve the number of questions to return from the query parameter
        num_of_questions = request.GET.get("numOfQuestions", default=len(unseen_item_list))
        try:
            num_of_questions = int(num_of_questions)
        except ValueError:
            return JsonResponse({"error": "Invalid number format"}, status=400)

        # Return only the requested number of questions
        limited_list = unseen_item_list[:num_of_questions]

        return JsonResponse(limited_list, safe=False)

    else:
        return http_error_response()


def test_version(request):
    print("\tReceived request at 'test_version' endpoint")  # Debugging output
    if request.method == "GET" and is_valid_header(request):
        front_end_version = request.GET.get("frontEndVersion", default="")
        is_version_match = front_end_version == "0.0.1"
        return JsonResponse({"version_match": is_version_match})
    else:
        return http_error_response()
