import re
import json

text = """
의미: other
예문:
[형] [형] 또 다른, 그 밖의
번역:
What other options do you have?

의미: mean
예문:
[형] [동] 의미하다
번역:
LOL means 'laugh out loud.'

의미: such
예문:
[형] [형] 그러한, ~와 같은
번역:
There is no such thing as a free lunch.

의미: still
예문:
[형] [부] 아직도, 여전히
번역:
He is 80, but still robust.

의미: lot
예문:
[형] [명] 많음, 다수
번역:
She shed a lot of tears during the funeral.

의미: leave
예문:
[형] [동] 떠나다, 남기다
번역:
You have to leave now, otherwise you'll miss the train.

의미: interest
예문:
[형] [명] 관심, 흥미
번역:
It is very important to pursue your own interest.

의미: each
예문:
[형] [형] 각각의
번역:
You should allocate the same amount of time to each question.

의미: include
예문:
[형] [동] 포함하다
번역:
This package includes flights, meals, and accommodation.

의미: seem
예문:
[형] [동] ~인 것 같다
번역:
It seems reasonable to impose tax on alcohol.

의미: let
예문:
[형] [동] ~하도록 허락하다
번역:
Let me sketch out the outline of the project.

의미: set
예문:
[형] [동] 놓다, (기계를) 맞추다
번역:
Set a trap to catch mice.

의미: follow
예문:
[형] [동] 뒤따르다
번역:
Q&A session will follow after the presentation.

의미: state
예문:
[형] [명] 상태
번역:
No one would buy the laptop because it is in a terrible state.

의미: provide
예문:
[형] [동] 제공하다
번역:
The hotel provides free breakfast for guests.

의미: government
예문:
[형] [명] 정부
번역:
The government needs to take care of its citizens.

의미: increase
예문:
[형] [동] 증가하다
번역:
House prices have increased sharply. 

의미: result
예문:
[형] [명] 결과
번역:
The result was pretty satisfying.

의미: happen
예문:
[형] [동] (사건)우연히 일어나다
번역:
We don't know what will happen tomorrow.

의미: offer
예문:
[형] [동] 제공하다
번역:
The workshop will offer free lunch to everyone. 

의미: lead
예문:
[형] [동] 이끌다, 지휘하다
번역:
A leader is a person who leads a group of people.

의미: less
예문:
[형] [부] 더 적게
번역:
Hybrid vehicles use less fuel. 

의미: reason
예문:
[형] [명] 이유, 근거
번역:
There are several different reasons why a dog will dig.

의미: spend
예문:
[형] [동] (돈/시간) 쓰다
번역:
They spent a substantial amount of money just for a day.

의미: experience
예문:
[형] [명] 경험
번역:
Tolstoy's experiences of war had a profound effect on his work.

의미: once
예문:
[형] [부] 한 번, 언젠가
번역:
I go jogging once a week.

의미: able
예문:
[형] [형] ~을 할 수 있는, 유능한
번역:
I was able to overcome fear of failure.

의미: support
예문:
[형] [동] 지지하다, 후원하다
번역:
It is essential to cite examples to support your argument.

의미: quite
예문:
[형] [부] 꽤, 상당히
번역:
I have quite a good relationship with my kids.

의미: sure
예문:
[형] [형] 확신하는
번역:
Make sure you put a book in the middle of the box.

의미: term
예문:
[형] [명] 기간, 용어
번역:
Medical terms are too difficult to understand.

의미: public
예문:
[형] [형] 대중의, 공공의
번역:
Politicians know how to manipulate public opinion.

의미: possible
예문:
[형] [형] 가능한
번역:
It is possible to drink two liters of water a day.

의미: rather
예문:
[형] [부] 다소, 오히려
번역:
I feel sleepy rather than tired.

의미: view
예문:
[형] [명] 전망, 견해, 의견
번역:
What's your view about LGBT?

의미: consider
예문:
[형] [동] 잘 생각하다, ~로 여기다
번역:
I consider myself confident, not cocky. 

의미: local
예문:
[형] [형] 지역의
번역:
I always try local food when travelling abroad.

의미: concern
예문:
[형] [명] 걱정, 관심
번역:
Shinzo Abe expressed growing concern about North Korea's nuclear program.

의미: product
예문:
[형] [명] 상품, 제품
번역:
I don't like dairy products, such as butter or cheese.

의미: lose
예문:
[형] [동] 지다, 잃다
번역:
I've lost my appetite. 

의미: continue
예문:
[형] [동] 계속하다
번역:
After taking a sip of water, he continued his speech.

의미: whole
예문:
[형] [형] 전체의, 모두의
번역:
a whole new perspective on life

의미: yet
예문:
[형] [부] 아직 (안 함, 못 함)
번역:
The time of my glory has not yet come.

의미: rate
예문:
[형] [명] 속도, 비율
번역:
My heart rate goes up to 180 bpm when running.

의미: expect
예문:
[형] [동] 기대하다
번역:
The price is somewhat cheaper than I expected.

의미: effect
예문:
[형] [명] 효과, 영향
번역:
Tolstoy's experiences of war had a profound effect on his work.

의미: sort
예문:
[형] [명] 종류
번역:
I like all sorts of food.

의미: ever
예문:
[형] [부] 언제나, 영원히
번역:
Have you ever been to Australia?

의미: cause
예문:
[형] [동] 야기하다, 원인을 제공하다
번역:
Heavy traffic causes delays on roads.

의미: deal
예문:
[형] [명] 거래
번역:
I made a deal to open my shop.

의미: allow
예문:
[형] [동] 허락하다
번역:
Please, allow me to go home.

의미: soon
예문:
[형] [부] 곧
번역:
It's going to rain soon.

의미: probably
예문:
[형] [부] 아마도
번역:
We will probably skip Disneyland on this trip.

의미: suggest
예문:
[형] [동] 제안하다
번역:
She suggested her husband take the pill.

의미: matter
예문:
[형] [명] 문제, 일
번역:
What's the matter with you?

의미: value
예문:
[형] [명] 가치, 중요성
번역:
The value of gold is decreasing.

의미: force
예문:
[형] [동] 강요하다
번역:
My father forced me to study English.

의미: several
예문:
[형] [형] 몇몇의
번역:
I know several good friends.

의미: develop
예문:
[형] [동] 개발하다
번역:
Chicago developed into a big city in the late 1800s.

의미: bit
예문:
[형] [명] 작은 조각
번역:
a little bit of faith

의미: figure
예문:
[형] [명] 숫자
번역:
unemployment figures

의미: language
예문:
[형] [명] 언어
번역:
Constant practice is the only way to learn a foreign language.

의미: subject
예문:
[형] [명] 주제, 과목
번역:
My favorite subject was science.

의미: minute
예문:
[형] [명] (시간)분, 잠깐
번역:
She hesitated for a minute and said, 'no.'

의미: either
예문:
[형] [대] (둘 중)어느 하나
번역:
The statement is either true or false.

의미: remain
예문:
[형] [동] (그대로) 남아 있다
번역:
Please, remain seated until the airplane comes to a full stop.

의미: involve
예문:
[형] [동] 관련시키다, 포함하다
번역:
Building a house involves a lot of work.

의미: reach
예문:
[형] [동] 도착하다, 닿다
번역:
Most UFC fighters reach their peak in their mid-20s.

의미: social
예문:
[형] [형] 사회의, 사교의
번역:
A handshake is a social convention.

의미: period
예문:
[형] [명] 기간, 시대
번역:
Japanese words used in Korea are a legacy from the colonial period.

의미: create
예문:
[형] [동] 창조하다
번역:
God created the Heaven and the Earth.

의미: political
예문:
[형] [형] 정치의
번역:
Education is a major political issue.

의미: receive
예문:
[형] [동] 받다
번역:
receive unemployment benefits

의미: moment
예문:
[형] [명] 순간
번역:
I bought an Apple Watch on the spur of the moment.

의미: policy
예문:
[형] [명] 정책
번역:
The apartment has adopted a strict no-smoking policy.

의미: further
예문:
[형] [부] 더 멀리로
번역:
Further research will confirm the hypothesis.

의미: require
예문:
[형] [동] 요구하다, 필요로 하다
번역:
A deposit of 30% is required to buy the car.

의미: general
예문:
[형] [형] 일반적인, 전반적인
번역:
a general idea about learning and teaching

의미: appear
예문:
[형] [동] 나타나다, ~인 것 같다
번역:
A boy suddenly appeared in the road.

의미: individual
예문:
[형] [형] 개인의
번역:
individual taste

의미: perhaps
예문:
[형] [부] 아마, 어쩌면
번역:
Perhaps, it may rain tomorrow.

의미: law
예문:
[형] [명] 법
번역:
obey the law

의미: research
예문:
[형] [명] 연구, 조사
번역:
field research

의미: position
예문:
[형] [명] 위치, 자세, 입장
번역:
What's your position?

의미: situation
예문:
[형] [명] 상황
번역:
Before judging the current situation, you should first look at it in context.

의미: account
예문:
[형] [명] 계좌, 설명
번역:
His account was badly distorted by the press.

의미: major
예문:
[형] [형] 주요한, 대다수의
번역:
Education is a major political issue.

의미: sometimes
예문:
[형] [부] 때때로, 가끔
번역:
I sometimes ignore phone calls.

의미: forward
예문:
[형] [부] 앞쪽으로
번역:
She leaned forward, her elbows resting on the table.

의미: main
예문:
[형] [형] 주된, 중요한
번역:
In the movie, the main character was buried alive.

의미: description
예문:
[형] [명] 묘사, 서술, 설명
번역:
The beauty of the black hole defies description.

의미: available
예문:
[형] [형] 이용할 수 있는
번역:
Tickets are available from the website.

의미: especially
예문:
[형] [부] 특히
번역:
Art books are expensive, especially if they have many color photos.

의미: rise
예문:
[형] [동] 일어나다, 뜨다
번역:
If the sun rose in the west,

의미: maybe
예문:
[형] [부] 아마, 어쩌면
번역:
Maybe, Arnold Schwarzenegger could not be a human.

의미: community
예문:
[형] [명] 지역사회, 집단
번역:
a community where peace, justice, and equity win

의미: else
예문:
[형] [형] 그 밖의, 다른
번역:
In her dream, she was enclosed by fog so dense that she could see nothing else.

의미: particular
예문:
[형] [형] 특별한
번역:
For no particular reason, she felt acute pain in her neck. 

의미: detail
예문:
[형] [명] 세부사항
번역:
Tell me every detail of the accident

의미: practice
예문:
[형] [명] 연습, 실행
번역:
Practice makes perfect.

의미: raise
예문:
[형] [동] 들어올리다
번역:
You raise me up.

의미: explain
예문:
[형] [동] 설명하다
번역:
Can you explain everything about the accident?

의미: outside
예문:
[형] [형] 바깥쪽의
번역:
A large crowd has assembled outside the Blue House.

의미: economic
예문:
[형] [형] 경제의
번역:
economic crisis in 1997

의미: site
예문:
[형] [명] (사건)현장, (건축)부지
번역:
a site for a new apartment

의미: approach
예문:
[형] [명] 접근
번역:
in the approach of winter

의미: charge
예문:
[형] [동] (요금을) 청구하다
번역:
The museum charges an entrance fee.

의미: finally
예문:
[형] [부] 마침내
번역:
After several delays the airplane finally took off at 11 pm.

의미: claim
예문:
[형] [명] 주장, 요구
번역:
claims for compensation

의미: relationship
예문:
[형] [명] 관계
번역:
I have quite a good relationship with my kids.

의미: amount
예문:
[형] [명] 양
번역:
You should allocate the same amount of time to each question.

의미: improve
예문:
[형] [동] 향상시키다, 나아지다
번역:
What should I do to improve my English?

의미: regard
예문:
[형] [동] ~로 여기다
번역:
Plagiarism is regarded as unethical.

의미: range
예문:
[형] [명] 범위
번역:
This pill is effective against a range of bacteria.

의미: quality
예문:
[형] [명] 품질, 질
번역:
high quality images

의미: opportunity
예문:
[형] [명] 기회
번역:
a rare opportunity to meet celebrities 

의미: accord
예문:
[형] [동] 일치하다, 부합하다
번역:
according to the police, 

의미: therefore
예문:
[형] [부] 그러므로
번역:
Neurons need a lot of energy and therefore consume a lot of calories.

의미: fund
예문:
[형] [명] 자금
번역:
raise funds for the poor

의미: rest
예문:
[형] [명] 휴식
번역:
Why don't we take a rest?

의미: industry
예문:
[형] [명] 산업
번역:
service industry

의미: education
예문:
[형] [명] 교육
번역:
tertiary education

의미: measure
예문:
[형] [동] 측정하다
번역:
We can measure how much energy neurons need.

의미: serve
예문:
[형] [동] 제공하다, 근무하다
번역:
soldiers who have served their country

의미: national
예문:
[형] [형] 국가의, 국립의
번역:
Seoul National University

의미: security
예문:
[형] [명] 보안, 안전
번역:
the National Security Agency

의미: benefit
예문:
[형] [명] 혜택
번역:
receive unemployment benefits

의미: trade
예문:
[형] [명] 무역하다, 교환하다
번역:
trading company

의미: vote
예문:
[형] [명] 투표
번역:
I voted for the progress party

의미: instead
예문:
[형] [부] 그 대신에
번역:
you can subscribe MS-Office programs, instead of buying them.

의미: usually
예문:
[형] [부] 보통
번역:
Usually, Koreans eat chicken with beer.

의미: performance
예문:
[형] [명] 공연, 성과
번역:
his performance in academic work

의미: accept
예문:
[형] [동] 받아들이다
번역:
I accepted her apology.

의미: mention
예문:
[형] [동] 언급하다
번역:
Don't mention about salary.

의미: choice
예문:
[형] [명] 선택
번역:
We have two choices.

의미: common
예문:
[형] [형] 흔한, 공통의
번역:
We have many things in common.

의미: demand
예문:
[형] [동] 요구하다
번역:
Marathon is physically demanding.

의미: material
예문:
[형] [명] 재료, 소재
번역:
raw material

의미: limit
예문:
[형] [명] 한계, 제한
번역:
One of my favorite quotes is: "the limits of my language are the limits of my world."

의미: due
예문:
[형] [형] ~로 인해
번역:
He was able to succeed due to his efforts.

의미: effort
예문:
[형] [명] 노력
번역:
He was able to succeed due to his efforts.

의미: attention
예문:
[형] [명] 주의, 관심
번역:
May I have your attention, please.

의미: complete
예문:
[형] [동] 완료하다
번역:
You complete me. 

의미: reduce
예문:
[형] [동] 줄이다
번역:
How can I reduce my sleeping hours?

의미: personal
예문:
[형] [형] 개인적인
번역:
a personal computer

의미: patient
예문:
[형] [형] 참을성 있는
번역:
You need to be more patient.

의미: current
예문:
[형] [형] 현재의, 지금의
번역:
current events

의미: century
예문:
[형] [명] 세기(100년)
번역:
We live in the 21st century.

의미: evidence
예문:
[형] [명] 증거
번역:
the evidence of his being a murderer

의미: exist
예문:
[형] [동] 존재하다
번역:
Do you believe that aliens exist?

의미: similar
예문:
[형] [형] 비슷한, 닮은
번역:
I have a similar experience like yours.

의미: contact
예문:
[형] [명] 접촉, 연락
번역:
contact information

의미: prepare
예문:
[형] [동] 준비하다
번역:
It's impossible to prepare ourselves for the future.

의미: response
예문:
[형] [명] 대답, 반응
번역:
in response to your question

의미: piece
예문:
[형] [명] 조각
번역:
It's a piece of cake!

의미: suppose
예문:
[형] [동] 추측하다, 가정하다
번역:
What am I supposed to do?

의미: apply
예문:
[형] [동] 지원하다, 적용되다
번역:
I'd like to apply for a small business loan.

의미: president
예문:
[형] [명] 대통령, 사장
번역:
the president of Korea

의미: compare
예문:
[형] [동] 비교하다, 비유하다
번역:
The police compared his fingerprints with those found at the crime scene.

의미: court
예문:
[형] [명] 법정, 경기장
번역:
a court of law

의미: knowledge
예문:
[형] [명] 지식
번역:
She has much knowledge of Korean history.

의미: laugh
예문:
[형] [동] (소리내어) 웃다
번역:
LOL means 'laugh out loud.'

의미: source
예문:
[형] [명] 원천, 원인
번역:
the main source of income

의미: manage
예문:
[형] [동] 관리하다
번역:
Managing a classroom is not easy.

의미: firm
예문:
[형] [형] 딱딱한, 확고한
번역:
A firm mattress is better than soft one.

의미: cell
예문:
[형] [명] 세포
번역:
red blood cells

의미: article
예문:
[형] [명] 기사, 조항, 물품
번역:
current event articles for kids

의미: attack
예문:
[형] [명] 공격
번역:
a bomb attack(terror)

의미: foreign
예문:
[형] [형] 외국의
번역:
My wife works for a foreign company.

의미: surprise
예문:
[형] [동] 놀라게 하다
번역:
The bomb attack surprised everybody.

의미: feature
예문:
[형] [명] 특징
번역:
Lotte World Tower has become the most popular feature of Jamsil.

의미: factor
예문:
[형] [명] 요소, 원인
번역:
The weather will be a crucial factor in tomorrow's game.

의미: recently
예문:
[형] [부] 최근에
번역:
Have you met any Chinese people recently?

의미: affect
예문:
[형] [동] ~에 영향을 주다
번역:
The weather will affect tomorrow's game.

의미: drop
예문:
[형] [명] (물)방울
번역:
I like the sound of rain drops.

의미: relate
예문:
[형] [동] 관련시키다
번역:
He is trying to relate Life of Pi to real life.

의미: official
예문:
[형] [형] 공식적인, 공무상의
번역:
an official announcement

의미: private
예문:
[형] [형] 개인적인, 비밀의
번역:
What a great private tutor!

의미: pause
예문:
[형] [명] 잠시 멈춤
번역:
"Yes," she replied without pausing for thought.

의미: opinion
예문:
[형] [명] 의견, 견해
번역:
My wife always asks my opinion on every important decision.

의미: represent
예문:
[형] [동] 대표하다
번역:
Mickey Mouse represents Disneyland.

의미: international
예문:
[형] [형] 국제의
번역:
the International Standard Book Number (ISBN)

의미: contain
예문:
[형] [동] 들어있다
번역:
Coca-Cola contains sugar.

의미: notice
예문:
[형] [명] 주의, 통지, 공고
번역:
There is a notice saying, 'watch your head.'

의미: wonder
예문:
[형] [명] 놀라움
번역:
the Seven Wonders of the Ancient World

의미: structure
예문:
[형] [명] 구조, 조직
번역:
The social structure of India is called the caste system.

의미: section
예문:
[형] [명] 부분, 부서
번역:
the business section of the New York Times

의미: exactly
예문:
[형] [부] 정확히
번역:
It's exactly 2 am.

의미: plant
예문:
[형] [명] 식물
번역:
water the plants

의미: press
예문:
[형] [명] 언론
번역:
the freedom of the press

의미: necessary
예문:
[형] [형] 필수의, 필요한
번역:
It's necessary to wear a tie.

의미: region
예문:
[형] [명] 지역, 부분, 범위
번역:
How clean the region is!

의미: influence
예문:
[형] [동] 영향을 미치다
번역:
Many writers are influenced by Shakespeare. 

의미: respect
예문:
[형] [동] 존경하다
번역:
I respect him for his honesty.

의미: various
예문:
[형] [형] 다양한
번역:
A rainbow has various colors.

의미: thus
예문:
[형] [부] 그러므로, 따라서
번역:
The man who dies thus rich dies disgraced.

의미: skill
예문:
[형] [명] 기술, 능력
번역:
I met a man whose writing skill is outstanding. 

의미: attempt
예문:
[형] [명] 시도
번역:
After several attempts, the cat finally managed to get the fish.

의미: medium
예문:
[형] [형] 중간의
번역:
a man of medium build

의미: average
예문:
[형] [명] 평균, 보통 수준
번역:
Jane is in her late twenties and of average height.

의미: character
예문:
[형] [명] 성격, 주인공, 문자
번역:
Who's your favorite Marvel character?

의미: establish
예문:
[형] [동] 설립하다, 확립하다
번역:
When was Apple established? / on April 1, 1976

의미: indeed
예문:
[형] [부] 참으로, 정말
번역:
Thank you very much indeed.

의미: certain
예문:
[형] [형] 특정한
번역:
Many animals breed only at certain times of the year.

의미: fit
예문:
[형] [동] 꼭 맞다, 적합하다
번역:
This hat does not fit him very well.

의미: function
예문:
[형] [명] 기능
번역:
What's the function of the pancreas?

의미: image
예문:
[형] [명] 이미지, 형태
번역:
Human beings are created in the image of God.

의미: clue
예문:
[형] [명] 단서, 힌트
번역:
Police have found a vital clue.

의미: behavior
예문:
[형] [명] 행동, 태도
번역:
the effects of LSD on human behavior

의미: addition
예문:
[형] [명] 추가
번역:
In addition to his salary, he got a bonus of $10,000 this year. 

의미: determine
예문:
[형] [동] 결정하다, 결심하다
번역:
The US president, Donald Trump, determined who would do the job.

의미: cute
예문:
[형] [형] 귀여운, 예쁜
번역:
A cute little puppy jumped up and licked her face.

의미: population
예문:
[형] [명] 인구
번역:
The world population is increasing.

의미: environment
예문:
[형] [명] 환경
번역:
He said, "we must protect the environment."

의미: contract
예문:
[형] [명] 계약, 계약서
번역:
It is believed that the contract is invalid.

의미: hang
예문:
[형] [동] 매달다, 걸다
번역:
She hung a towel on the hook on the wall.

의미: comment
예문:
[형] [명] 논평, 언급
번역:
If BTS left a comment on your Facebook, 

의미: occur
예문:
[형] [동] 발생하다
번역:
A mistake has occurred.

의미: borrow
예문:
[형] [동] 빌리다
번역:
It's not a good idea to borrow someone else's car.

의미: significant
예문:
[형] [형] 상당한, 중요한
번역:
What is the most significant change in iOS 15?

의미: drug
예문:
[형] [명] 약, 마약
번역:
Lysergic acid diethylamide (LSD) is a hallucinogenic drug.

의미: series
예문:
[형] [명] 연속, 시리즈
번역:
a series of misfortunes

의미: direct
예문:
[형] [형] 직접적인, 직행의
번역:
He couldn't answer the direct call from the radio DJ

의미: bug
예문:
[형] [명] 벌레
번역:
A bug is crawling up your leg!

의미: success
예문:
[형] [명] 성공
번역:
What is the definition of success?

의미: lack
예문:
[형] [명] 결핍
번역:
Lack of time kept me from visiting the store.

의미: cheap
예문:
[형] [형] 값싼
번역:
The price is somewhat cheaper than I expected.

의미: review
예문:
[형] [동] 복습하다, 검토하다
번역:
You have to review what you've learned so far every day.

의미: depend
예문:
[형] [동] 의존하다, ~에 달려 있다
번역:
Happiness depends on your mindset and attitude.

의미: recognize
예문:
[형] [동] 알아보다, 인정하다
번역:
"Nala? It's me, Simba!" Simba recognized Nala.

의미: clever
예문:
[형] [형] 영리한, 기민한
번역:
He devised a clever plan to escape from the prison.

의미: purpose
예문:
[형] [명] 목적
번역:
It is very important to find the purpose of life.

의미: department
예문:
[형] [명] 부문, 부서
번역:
Helen from the marketing department

의미: gain
예문:
[형] [동] 얻다, 늘다
번역:
Yong gained a master's degree in applied linguistics.

의미: argue
예문:
[형] [동] 논쟁하다, 주장하다
번역:
I heard the neighbors arguing.

의미: cloud
예문:
[형] [명] 구름
번역:
The sun went behind a dark cloud.

의미: machine
예문:
[형] [명] 기계
번역:
I want to learn how to use this sewing machine.

의미: crazy
예문:
[형] [형] 미친, 정신나간
번역:
You might think this is an absolutely crazy idea, but…

의미: achieve
예문:
[형] [동] 이루다, 성취하다
번역:
My sister-in-law eventually achieved her goal of becoming a professor.

의미: prove
예문:
[형] [동] 증명하다
번역:
Prove your innocence!

의미: cry
예문:
[형] [동] 울다, (절규) 외치다
번역:
"I wouldn't cry," he boasted.

의미: stuff
예문:
[형] [명] 물건
번역:
I've got some sticky stuff on my shoe.

의미: wide
예문:
[형] [형] 넓은
번역:
I should've bought a wider TV.

의미: culture
예문:
[형] [명] 문화
번역:
I love meeting people from different cultures.

의미: method
예문:
[형] [명] 방법
번역:
We should try a different method.

의미: analysis
예문:
[형] [명] 분석
번역:
The company used statistical analysis in examining customer behavior.

의미: election
예문:
[형] [명] 선거
번역:
Korea's 21st legislative election is held on 15 April 2020.

의미: dangerous
예문:
[형] [형] 위험한, 위험을 주는
번역:
Head-on collisions are probably the most dangerous type of crashes.

의미: deep
예문:
[형] [형] 깊은
번역:
The deep sea remains almost entirely unknown.

의미: challenge
예문:
[형] [명] 도전
번역:
In 2019, the keyword of my family was 'challenge.'

의미: nearly
예문:
[형] [부] 거의
번역:
I was nearly hit by a car.

의미: statement
예문:
[형] [명] 성명, 진술서
번역:
an official statement on his resignation

의미: link
예문:
[형] [동] 연결하다
번역:
Birth defects are linked to smoking during pregnancy.

의미: discussion
예문:
[형] [명] 논의, 토의
번역:
How important is it for students to actively participate in class discussions?

의미: advantage
예문:
[형] [명] 유리한 점, 강점
번역:
Identify your competitive advantage succinctly.

의미: failure
예문:
[형] [명] 실패
번역:
I was able to overcome fear of failure.

의미: strike
예문:
[형] [동] 치다
번역:
A snowball struck her on the face. 

의미: seek
예문:
[형] [동] 찾다, 구하다
번역:
Many Iraqi people were seeking refuge from the war.

의미: ability
예문:
[형] [명] 능력, 재능
번역:
Many animals get the ability to walk at birth. 

의미: unit
예문:
[형] [명] 단위, 단원
번역:
an intensive care unit (ICU)

의미: hell
예문:
[형] [명] 지옥
번역:
These past few days have been a living hell.

의미: hold
예문:
[형] [동] 붙잡고 있다
번역:
I need to piss(pee). I can't hold it!

의미: release
예문:
[형] [동] 석방하다, 공개하다
번역:
The birds are eventually released into the wild.

의미: tax
예문:
[형] [명] 세금
번역:
A fat tax is a tax on foods or drinks considered unhealthy.

의미: solution
예문:
[형] [명] 해결책
번역:
Is a fat tax a solution for obesity?

의미: capital
예문:
[형] [명] 수도, 자본, 대문자
번역:
Write your surname in capital letters.

의미: popular
예문:
[형] [형] 인기있는, 대중의
번역:
I wasn't popular at school.

의미: honest
예문:
[형] [형] 정직한
번역:
사망여우 persists in reporting dishonest company behaviors. 

의미: specific
예문:
[형] [형] 구체적인, 특정한
번역:
We need very specific instructions.

의미: fear
예문:
[형] [명] 공포
번역:
I didn't gamble, for fear of losing money.

의미: aim
예문:
[형] [동] 목표로 하다, 겨누다
번역:
The gun was aimed at him.

의미: insert
예문:
[형] [명] (사이에) 삽입하다
번역:
Insert a coin into the slot.

의미: target
예문:
[형] [명] 목표
번역:
The twin buildings were the targets for the terrorists.

의미: degree
예문:
[형] [명] 온도, 각도, 정도
번역:
Preheat the oven to 180 degrees Celsius.

의미: pull
예문:
[형] [동] 당기다, 끌다
번역:
Drumlin pulled the plug.

의미: invite
예문:
[형] [동] 초대하다
번역:
Spouses have been invited to the company excursion.

의미: access
예문:
[형] [명] 접근
번역:
All people should have access to clean water.

의미: treat
예문:
[형] [동] 대하다, 치료하다
번역:
She got angry at the way she had been treated.

의미: identify
예문:
[형] [동] (신원 등) 확인/알게 하다
번역:
Identify your competitive advantage succinctly.

의미: jewelry
예문:
[형] [명] 보석류, 장신구
번역:
Thieves broke into the jewelry shop and stole all the jewelry.

의미: loss
예문:
[형] [명] 손실, 손해
번역:
Kobe Bryant's death is a great loss for all Americans.

의미: pressure
예문:
[형] [명] 압력, 압박
번역:
The EU put pressure on Russia.

의미: lazy
예문:
[형] [형] 게으른
번역:
Lazy people are likely to be smarter.

의미: supply
예문:
[형] [명] 공급, 공급품
번역:
the law of supply and demand

의미: village
예문:
[형] [명] 마을
번역:
Welcome to our humble village!

의미: leaf
예문:
[형] [명] 잎, 잎사귀
번역:
Fertilizer promotes leaf growth.

의미: worth
예문:
[형] [형] ~할 만한 가치가 있는
번역:
Sapiens is worth reading.

의미: express
예문:
[형] [동] 표현하다
번역:
Words can't express my happiness!

의미: indicate
예문:
[형] [동] 나타내다
번역:
"That's Jane," said Tom, indicating a girl at the door.

의미: attend
예문:
[형] [동] 참석하다
번역:
Are you going to attend the meeting today?

의미: move
예문:
[형] [동] 움직이다
번역:
I moved quietly to avoid scaring the pigeons off.

의미: investment
예문:
[형] [명] 투자, 투자액
번역:
Chinese investment in the Jeju property market started to skyrocket in 2011.

의미: organize
예문:
[형] [동] 조직하다, 체계를 세우다
번역:
how to organize your day

의미: narrow
예문:
[형] [형] (폭) 좁은
번역:
Narrow corridors make people move around the ship in a safe manner.

의미: promise
예문:
[형] [명] 약속
번역:
The company promised me a bonus this year.

의미: potential
예문:
[형] [형] 잠재적인, 가능성 있는
번역:
Drowsy driving is a potential danger to other road users.

의미: nasty
예문:
[형] [형] 끔찍한, 최악의
번역:
The UFC fighter got a nasty facial injury in the bout.

의미: trouble
예문:
[형] [명] 문제, 어려움
번역:
Their marriage is in trouble.

의미: obtain
예문:
[형] [동] 얻다, 획득하다
번역:
You will need to obtain permission from the CEO.

의미: suffer
예문:
[형] [동] 고통 받다, 겪다
번역:
Some people suffer from rare skin diseases.

의미: strategy
예문:
[형] [명] 전략, 계획
번역:
Viral marketing is a kind of marketing strategy. 

의미: peace
예문:
[형] [명] 평화
번역:
Let's pray for peace.

의미: tend
예문:
[형] [동] ~하는 경향이 있다
번역:
Some BMW cars tend to overheat in the summer.

의미: advance
예문:
[형] [명] 전진, 진보
번역:
The hotel is usually booked up a year in advance.

의미: punishment
예문:
[형] [명] 벌, 처벌
번역:
Many schools have a system of rewards and punishments to encourage good behavior.

의미: match
예문:
[형] [동] 맞다, 어울리다
번역:
To match the wall, I bought a wooden bookshelf.

의미: root
예문:
[형] [명] 뿌리, 근원
번역:
The love of money is the root of all evil.

의미: avoid
예문:
[형] [동] 피하다
번역:
To avoid road accidents, road safety is taught to new drivers.

의미: throw
예문:
[형] [동] 던지다
번역:
The singer threw himself to the crowd. 

의미: task
예문:
[형] [명] 업무
번역:
Dogs can be trained to do simple tasks.

의미: normal
예문:
[형] [형] 정상적인
번역:
I don't want a normal life.

의미: rotate
예문:
[형] [동] 돌리다, 회전시키다
번역:
Rotate the plate halfway through the baking time.

의미: associate
예문:
[형] [동] 연관짓다
번역:
Often, we associate God with the image of a father.

의미: positive
예문:
[형] [형] 긍정적인, 낙관적인
번역:
I always want to be positive.

의미: option
예문:
[형] [명] 선택(권)
번역:
What other options do you have?

의미: scientist
예문:
[형] [명] 과학자
번역:
Scientists are trying to trace the origin of life on earth.

의미: huge
예문:
[형] [형] 거대한
번역:
Big data means a huge mass of data.

의미: instance
예문:
[형] [명] 보기, 사례
번역:
We hear many instances of bullying in public schools.

의미: serious
예문:
[형] [형] 심각한
번역:
Gambling could have serious consequences.

의미: refer
예문:
[형] [동] 언급하다, 참고하다
번역:
Please, refer to the table on page 33.

의미: quarter
예문:
[형] [명] 1/4
번역:
Roughly, one quarter of Korea's population live in Seoul.

의미: assume
예문:
[형] [동] 가정하다
번역:
Assume that you were the president of Korea.

의미: shape
예문:
[형] [명] 모양, 형태
번역:
A mosquito coil is a spiral shape.

의미: doubt
예문:
[형] [동] 의심하다
번역:
You can complain, but I doubt if it will make any difference.

의미: competition
예문:
[형] [명] 경쟁, 시합
번역:
There is intense competition for the job.

의미: shelf
예문:
[형] [명] 선반
번역:
I need a room furnished with a long desk and a large bookshelf.

의미: theory
예문:
[형] [명] 이론
번역:
In theory, everyone has to pay taxes. 

의미: propose
예문:
[형] [동] 제안하다, 청혼하다
번역:
A lot of theories were proposed to explain the extinction of the dinosaurs.

의미: sin
예문:
[형] [명] 죄, 죄악
번역:
God forgives us our sins.

의미: document
예문:
[형] [명] 서류
번역:
Do you have the document that I asked you to bring? 

의미: obviously
예문:
[형] [부] 명백하게, 확실히
번역:
Obviously, the third world war would not happen.

의미: sock
예문:
[형] [명] 양말
번역:
a pair of ankle socks

의미: separate
예문:
[형] [형] 분리된, 별개의
번역:
Use separate knives for meat and vegetable. 

의미: solar
예문:
[형] [명] 태양의
번역:
All the orbits of the planets in the solar system are oval rather than circular.

의미: central
예문:
[형] [형] 중심의
번역:
He played a central role in the play.

의미: career
예문:
[형] [명] 직업, 경력
번역:
She built her teaching career in EBS. 

의미: speech
예문:
[형] [명] 연설
번역:
After taking a sip of water, he continued his speech.

의미: suck
예문:
[형] [동] 빨아들이다
번역:
Tim sucked up the last bit of milk shake with his straw.

의미: officer
예문:
[형] [명] 장교, 경찰관, 공무원
번역:
You should say, 'a police officer,' rather than 'a policeman.'

의미: profit
예문:
[형] [명] 이익
번역:
Making a profit is the most important objective of a business.

의미: taste
예문:
[형] [동] 맛이 나다, 맛이다
번역:
How come the water in a skull tasted so good? 

의미: protect
예문:
[형] [동] 보호하다
번역:
He said, "we must protect the environment."

의미: resource
예문:
[형] [명] 자원
번역:
Let me sketch out resources available at the moment.

의미: disease
예문:
[형] [명] 질병
번역:
A new coronavirus emerged from Wuhan seems one of the most contagious diseases on earth.

의미: thirsty
예문:
[형] [형] 목마른
번역:
Drink water frequently before you feel thirsty.

의미: balance
예문:
[형] [명] 균형, 조화
번역:
I nearly lost my balance when the bus suddenly stopped.

의미: damage
예문:
[형] [명] 손해, 손상
번역:
The earthquake caused severe damage to many buildings. 

의미: basis
예문:
[형] [명] 근거, 기초
번역:
His suggestion became the basis of this book.

의미: author
예문:
[형] [명] 저자
번역:
The author of Sapiens is Yuval Harari.

의미: ugly
예문:
[형] [형] 못생긴, 추한
번역:
Freddy Krueger looks very ugly.

의미: encourage
예문:
[형] [동] 격려하다, 권장하다
번역:
The manager encouraged us to attend the workshop.

의미: male
예문:
[형] [형] 남성의, 수컷의
번역:
It was a deep male voice.

의미: operate
예문:
[형] [동] 조작하다, 수술하다
번역:
This machine is designed to operate in all weather conditions.

의미: reflect
예문:
[형] [동] 반영하다, 반사하다
번역:
The streetlights are reflected in the car window.

의미: wet
예문:
[형] [형] (물) 젖은 
번역:
Wipe the table with a wet tissue.

의미: useful
예문:
[형] [형] 유용한
번역:
He gave me some useful advice.

의미: income
예문:
[형] [명] 소득
번역:
the main source of income

의미: wheat
예문:
[형] [명] 밀
번역:
Wheat is typically milled into flour.

의미: property
예문:
[형] [명] 재산, 부동산
번역:
Chinese investment in the Jeju property market started to skyrocket in 2011.

의미: previous
예문:
[형] [형] 이전의, 앞의
번역:
Jane has a child from a previous marriage.

의미: imagine
예문:
[형] [동] 상상하다
번역:
Imagine that you were the president of Korea.

의미: earn
예문:
[형] [동] (돈을) 벌다
번역:
I had many jobs to earn a living.

의미: workout
예문:
[형] [명] 운동 (시간) 
번역:
We should have a daily workout routine.

의미: post
예문:
[형] [명] 우편
번역:
You will soon get a new document by post.

의미: define
예문:
[형] [동] 정의하다, 규정하다
번역:
It is difficult to define good and evil using human criteria.

의미: worry
예문:
[형] [동] 걱정하다
번역:
I worry that all my effort might end in vain.

의미: conclusion
예문:
[형] [명] 결론
번역:
It is too early to reach a conclusion.

의미: wrong 
예문:
[형] [형] 잘못된, 틀린
번역:
There was speculation that Kim Jong-un was ill, but it was wrong.

의미: debate
예문:
[형] [명] 논쟁, 토론
번역:
widespread public debate

의미: object
예문:
[형] [명] 물건, 목표
번역:
the object of this game

의미: maintain
예문:
[형] [동] 유지하다, 지속하다
번역:
The politician wanted to maintain his position.

의미: discover
예문:
[형] [동] 발견하다, 알아내다
번역:
The remains of ancient civilization have been discovered in Turkey.

의미: prefer
예문:
[형] [동] ~을 더 선호하다
번역:
I prefer to travel by public transportation.

의미: extend
예문:
[형] [동] 연장하다, 뻗다
번역:
Subway Line 7 will be extended to Yangju by 2024.

의미: direction
예문:
[형] [명] 방향, 지시
번역:
Have you ever lost direction in the forest?

의미: facility
예문:
[형] [명] 시설
번역:
a research facility

의미: female
예문:
[형] [형] 여성의, 암컷의
번역:
A female mantis eats the male after mating.

의미: responsibility
예문:
[형] [명] 책임
번역:
With great power comes great responsibility.

의미: easily
예문:
[형] [부] 쉽게
번역:
Alcohol can easily remove sticker residue.

의미: legal
예문:
[형] [형] 법률의, 합법적인
번역:
What I have done is perfectly legal.

의미: conversation
예문:
[형] [명] 대화
번역:
a constructive conversation

의미: immediately
예문:
[형] [부] 즉시
번역:
Please remain calm and evacuate the building immediately.

의미: traditional
예문:
[형] [형] 전통의
번역:
I want to know what the traditional costume of Korea is.

의미: replace
예문:
[형] [동] 대체하다, 교체하다
번역:
replace a light bulb

의미: judge
예문:
[형] [동] 판단하다
번역:
Don't judge people by their looks.

의미: suddenly
예문:
[형] [부] 갑자기
번역:
A boy suddenly appeared in the road.

의미: generation
예문:
[형] [명] 세대
번역:
Samsung hopes 5-Generation Network will save its slumping profits this year.

의미: estimate
예문:
[형] [동] 추정하다
번역:
The police estimated the crowd at 10,000.

의미: purchase
예문:
[형] [동] 구매하다
번역:
You can even purchase a car online.

의미: shoot
예문:
[형] [동] 쏘다
번역:
The girl shot the villain when he pulled a gun on her.

의미: announce
예문:
[형] [동] 발표하다
번역:
He stood up and announced that he was Iron Man.

의미: independent
예문:
[형] [형] 독립적인
번역:
small independent bookshops

의미: recommend
예문:
[형] [동] 추천하다, 권하다
번역:
The doctor recommended him go to a bigger hospital.

의미: survey
예문:
[형] [명] 설문 조사
번역:
a survey conducted by Statistics Korea.

의미: exchange
예문:
[형] [명] 교환
번역:
Our refund and exchange policy is on the website.

의미: budget
예문:
[형] [명] 예산
번역:
We have a very tight budget.

의미: appropriate
예문:
[형] [형] 적절한, 알맞은
번역:
clothes appropriate for a job interview

의미: count
예문:
[형] [동] 세다
번역:
Count up how many people are in the crowd.

의미: content
예문:
[형] [명] 내용, 목차
번역:
a table of contents

의미: prevent
예문:
[형] [동] 예방하다, 막다
번역:
Can medical masks prevent coronavirus?

의미: element
예문:
[형] [명] 요소, 원소
번역:
the fifth element

의미: correct
예문:
[형] [동] 고치다, 수정하다
번역:
Please correct my pronunciation if it's wrong.

의미: medical
예문:
[형] [형] 의학의, 의료의
번역:
Medical terms are too difficult to understand.

의미: admit
예문:
[형] [동] 인정하다
번역:
You may not like Tom, but you have to admit that he is a nice guy.

의미: beat
예문:
[형] [동] (경기) 이기다
번역:
I easily beat my son at tennis.

의미: aware
예문:
[형] [형] 인식하고 있는
번역:
Many people were aware of the danger of corona virus. 

의미: advice
예문:
[형] [명] 충고
번역:
I should've followed my parents' advice.

의미: trial
예문:
[형] [명] 재판, 시도
번역:
A new drug is undergoing clinical trials.

의미: administration
예문:
[형] [명] 행정, 관리
번역:
the administration office of SNU

의미: complex
예문:
[형] [형] 복잡한
번역:
the complex structure of the brain

의미: text
예문:
[형] [명] 글
번역:
Read the text carefully.

의미: context
예문:
[형] [명] 맥락, 배경
번역:
Before judging the current situation, you should first look at it in context.

의미: ride
예문:
[형] [동] (차, 말) 타다
번역:
I've never ridden a horse.

의미: remove
예문:
[형] [동] 제거하다
번역:
how to remove a keycap

의미: conduct
예문:
[형] [동] 수행하다, 행동하다
번역:
conduct a survey

의미: equipment
예문:
[형] [명] 장비, 설비
번역:
I want to buy camping equipment.

의미: otherwise
예문:
[형] [부] 만약 그렇지 않다면
번역:
You have to leave now, otherwise you'll miss the train.

의미: extra
예문:
[형] [형] 추가의, 여분의
번역:
Do you have any extra copy?

의미: executive
예문:
[형] [형] 행정의, 관리의
번역:
Chief Executive Officer

의미: deliver
예문:
[형] [동] 배달하다
번역:
Do you deliver on weekends?

의미: primary
예문:
[형] [형] 주된, 초기의
번역:
the primary source of income

의미: inform
예문:
[형] [동] 알리다
번역:
You should inform the office of your new address.

의미: principle
예문:
[형] [명] 원칙
번역:
the basic principles of marketing

의미: straight
예문:
[형] [형] 곧은
번역:
She has long, straight brown hair.

의미: appeal
예문:
[형] [명] 간청, 호소
번역:
She is planning to make an appeal.

의미: highly
예문:
[형] [부] 매우, 대단히
번역:
Bill Gates is a highly successful businessman. 

의미: trust
예문:
[형] [명] 신뢰
번역:
There is a lack of trust between Tom and me. 

의미: flat
예문:
[형] [형] 평평한
번역:
A flat surface reflects light.

의미: absolutely
예문:
[형] [부] 전적으로, 틀림없이
번역:
You might think this is an absolutely crazy idea, but…

의미: flow
예문:
[형] [명] 흐름
번역:
swim against the flow of the water

의미: fair
예문:
[형] [형] 공평한, 타당한
번역:
a fair game

의미: negative
예문:
[형] [형] 부정적인, 적대적인
번역:
Smoking has a negative effect on health.

의미: relative
예문:
[형] [명] 친척
번역:
I didn't know that he is a distant relative of mine.

의미: alternative
예문:
[형] [명] 대안, 대체품
번역:
We need alternative approaches.

의미: pair
예문:
[형] [명] 똑같은 두 짝, 쌍
번역:
a pair of shoes

의미: attitude
예문:
[형] [명] 태도
번역:
Only a few people have a negative attitude to God's love.

의미: observe
예문:
[형] [동] 관찰하다
번역:
My son carefully observed the insect.

의미: sentence
예문:
[형] [명] 문장, 판결
번역:
It is difficult to sum up the speech in one sentence.

의미: progress
예문:
[형] [명] 진전, 진행
번역:
make slow but clear progress

의미: truth
예문:
[형] [명] 진실
번역:
The truth is that I didn't kill the boy.

의미: examine
예문:
[형] [동] 조사하다, 검사하다
번역:
The police examined how the boy was killed.

의미: lay
예문:
[형] [동] 내려놓다
번역:
Lay the paper flat on the table.

의미: transfer
예문:
[형] [동] 옮기다, 환승하다
번역:
I will be transferred to a local office.

의미: slightly
예문:
[형] [부] 약간
번역:
This color is slightly different to that color.

의미: overall
예문:
[형] [형] 전반적인, 전체의
번역:
the overall result of your IELTS test

의미: intend
예문:
[형] [동] ~할 작정이다, 의도하다
번역:
I intend to memorize this book within one month.

의미: regular
예문:
[형] [형] 정기적인
번역:
Regular exercise helps you stay fit.

의미: physical
예문:
[형] [형] 육체의, 물질적인
번역:
Physical exercise increases brain function.

의미: apart
예문:
[형] [부] 떨어져, 따로
번역:
Plant the seeds two inches apart.

의미: federal
예문:
[형] [형] 연방의, 연방 정부의
번역:
the federal government of the US

의미: reveal
예문:
[형] [동] 폭로하다, 드러내다
번역:
He revealed what I did last summer.

의미: status
예문:
[형] [명] 지위, 상태
번역:
Politicians used to enjoy their high social status.

의미: crime
예문:
[형] [명] 범죄
번역:
a high crime rate

의미: decline
예문:
[형] [동] 감소하다, 거절하다
번역:
The rate of crime committed by youth has been generally declining.

의미: decade
예문:
[형] [명] 10년
번역:
I have studied English for a decade.

의미: launch
예문:
[형] [명] 발사, 출시
번역:
To launch the application, double-click the icon.

의미: warn
예문:
[형] [동] 경고하다
번역:
Travelers to China are being warned about the danger of coronavirus infection.

의미: consumer
예문:
[형] [명] 소비자
번역:
Consumers will pay for delivery.

의미: institution
예문:
[형] [명] 기관, 제도
번역:
powerful institutions such as IMF

의미: spot
예문:
[형] [명] 장소, 점
번역:
Nari Park is a great tourist spot in Yangju.

의미: eventually
예문:
[형] [부] 결국
번역:
Eventually, the earth will be too hot to sustain life.

의미: excite
예문:
[형] [동] 흥분시키다
번역:
His speech excited me. 

의미: distance
예문:
[형] [명] 거리
번역:
The distance from Seoul to Daejon is not 100 kilometers, is it?

의미: grant
예문:
[형] [동] 승인하다
번역:
The bank granted a 200-million-won loan to her.

의미: feed
예문:
[형] [동] 먹이를 주다
번역:
Have you fed the fish?

의미: pain
예문:
[형] [명] 통증, 고통
번역:
For no particular reason, she felt acute pain in her neck. 

의미: ensure
예문:
[형] [동] 반드시 ~하게 하다, 보장하다
번역:
3 ways to ensure the safety of children

의미: satisfy
예문:
[형] [동] 만족시키다
번역:
The result was pretty satisfying.

의미: chief
예문:
[형] [명] 우두머리, (단체의)장
번역:
Chief Executive Officer

의미: expert
예문:
[형] [명] 전문가
번역:
To make use of big data, many companies need experts in statistics.

의미: wave
예문:
[형] [명] 파도, 파동
번역:
I watched the waves breaking on the rock.

의미: labor
예문:
[형] [명] 노동
번역:
Child labor is one of the oldest problems in our society.

의미: surface
예문:
[형] [명] 표면
번역:
A flat surface reflects light.

의미: edge
예문:
[형] [명] 가장자리, (칼)날
번역:
Don't push me 'cause I'm close to the edge.

의미: audience
예문:
[형] [명] 관객
번역:
The audience began to applaud.

의미: lift
예문:
[형] [동] 들어 올리다
번역:
I lifted my eyes so that I could see the building.

의미: procedure
예문:
[형] [명] 절차, 수술
번역:
What's the procedure for applying for a business loan?

의미: struggle
예문:
[형] [동] 애쓰다, 발버둥치다
번역:
She struggled to articulate her feeling.

의미: advertise
예문:
[형] [동] 광고하다
번역:
Many companies advertise on social media.

의미: select
예문:
[형] [동] 선택하다
번역:
a group of housewives selected at random

의미: surround
예문:
[형] [동] 둘러싸다
번역:
The house is surrounded by trees.

의미: extent
예문:
[형] [명] 정도, 크기
번역:
To what extent do you agree? 

의미: annual
예문:
[형] [형] 연간의, 해마다의
번역:
The graduation ceremony is an annual event.

의미: contrast
예문:
[형] [명] 차이, 대조
번역:
the social contrast between the rich and the poor

의미: roll
예문:
[형] [동] 구르다, 굴리다
번역:
The apples rolled along the corridor.

의미: conflict
예문:
[형] [명] 대립, 갈등
번역:
A small disagreement can provoke conflict between two people.

의미: entire
예문:
[형] [형] 전체의
번역:
Today is the best day in my entire life.

의미: shift
예문:
[형] [명] 변화, 이동
번역:
a big paradigm shift in education

의미: secretary
예문:
[형] [명] 비서
번역:
I need a secretary who can arrange my hectic schedule.

의미: defense
예문:
[형] [명] 방어, 변호
번역:
The immune system is the body's defense against infection.

의미: spread
예문:
[형] [동] 펼치다, 퍼뜨리다
번역:
The fire quickly spread to the store.

의미: nuclear
예문:
[형] [형] 핵의, 핵무기의
번역:
France's reliance on nuclear energy

의미: confirm
예문:
[형] [동] 확인하다
번역:
The study has confirmed that smoking can cause lung cancer.

의미: senior
예문:
[형] [형] 고위의, 연장자의
번역:
senior staff

의미: refuse
예문:
[형] [동] 거절하다
번역:
The computer refused to answer my question.

의미: emerge
예문:
[형] [동] 나타나다
번역:
A man emerged from the forest.

의미: island
예문:
[형] [명] 섬
번역:
Jeju Island has a unique dialect.

의미: neither
예문:
[형] [형] 어느 쪽도 ~아닌
번역:
Neither Newton nor Einstein perfectly understood the universe.

의미: survive
예문:
[형] [동] 살아남다, 견뎌 내다
번역:
He survived the terrorist attack.

의미: flight
예문:
[형] [명] 비행, 항공편
번역:
book a flight to Canada

의미: solve
예문:
[형] [동] 해결하다, 풀다
번역:
You solved all the problems, didn't you?

의미: neighbor
예문:
[형] [명] 이웃
번역:
Have you met your neighbors yet? 

의미: traffic
예문:
[형] [명] 교통, 교통량
번역:
Heavy traffic causes delays on roads.

의미: consequence
예문:
[형] [명] 결과
번역:
Gambling could have serious consequences.

의미: circumstance
예문:
[형] [명] 상황, 형편
번역:
exceptional circumstances

의미: mass
예문:
[형] [명] 덩어리
번역:
Big data means a huge mass of data.

의미: contribute
예문:
[형] [동] 기여하다
번역:
You can also contribute to society.

의미: adopt
예문:
[형] [동] 입양하다, 채택하다
번역:
The apartment has adopted a strict no-smoking policy.

의미: combine
예문:
[형] [동] 결합하다
번역:
Hydrogen combines with oxygen to form water.

의미: waste
예문:
[형] [명] 쓰레기, 낭비
번역:
If it is just us, it seems like an awful waste of space.

의미: hide
예문:
[형] [동] 숨기다, 숨다
번역:
My daughter hid my wallet in the drawer.

의미: meal
예문:
[형] [명] 식사
번역:
This package includes flights, meals, and accommodation.

의미: colleague
예문:
[형] [명] 동료
번역:
Kim is a colleague of mine.

의미: repeat
예문:
[형] [동] 반복하다
번역:
Repeat after me.

의미: equal
예문:
[형] [형] 동일한, 평등한
번역:
All things being equal, the simplest explanation tends to be the right one.

의미: extremely
예문:
[형] [부] 극도로
번역:
iPad mini is extremely useful for me.

의미: commercial
예문:
[형] [형] 상업의, 무역의
번역:
The film was a commercial success.

의미: duty
예문:
[형] [명] 의무, 임무
번역:
It is our duty to help people in need.

의미: strength
예문:
[형] [명] 힘, 강점
번역:
What are your strengths and weaknesses?

의미: connect
예문:
[형] [동] 연결하다, 관련시키다
번역:
Connect the cable to the printer.

의미: arrange
예문:
[형] [동] 정리하다, 준비하다
번역:
I need a secretary who can arrange my hectic schedule.

의미: scheme
예문:
[형] [명] (사회) 계획, 제도
번역:
an urban redevelopment scheme

의미: unfortunately
예문:
[형] [부] 불행하게도
번역:
Unfortunately, my first business was unsuccessful.

의미: brief
예문:
[형] [형] 간결한, 짧은
번역:
a brief introduction of World War 2

의미: demonstrate
예문:
[형] [동] 시위하다, 설명하다
번역:
Steve Jobs demonstrated how to use the new iPhone.

의미: appreciate
예문:
[형] [동] 고맙게 여기다
번역:
I'd appreciate it if you let me in.

의미: apparently
예문:
[형] [부] 듣자하니
번역:
Apparently, the couple are getting married soon.

의미: novel
예문:
[형] [명] 소설
번역:
Contact is a novel by Carl Sagan.

의미: union
예문:
[형] [명] 결합, 조합
번역:
I am planning to join the national union of English teachers.

의미: initial
예문:
[형] [형] 초기의
번역:
the initial stage of the disease

의미: pleasure
예문:
[형] [명] 즐거움
번역:
It's a great pleasure to meet you.

의미: critical
예문:
[형] [형] 비판적인, 중대한
번역:
My father was in a critical condition in hospital.

의미: gather
예문:
[형] [동] 모으다
번역:
About a hundred people gathered at the park.

의미: pop
예문:
[형] [동] 터지다, 나타나다
번역:
How do you pop a beer bottle cap off?

의미: essential
예문:
[형] [형] 필수의, 본질적인
번역:
It is essential to book the ticket in advance.

의미: desire
예문:
[형] [명] 욕구
번역:
Having the desire to run a marathon is a mystery.

의미: promote
예문:
[형] [동] 촉진하다, 홍보하다, 승진시키다
번역:
Fertilizer promotes leaf growth.

의미: employ
예문:
[형] [동] 고용하다
번역:
The company employs over 500 people.

의미: path
예문:
[형] [명] 길, 진로
번역:
a path less travelled

의미: attract
예문:
[형] [동] 끌다, 매혹하다
번역:
What attracted me most to the job was the flexible working hours system.

의미: engage
예문:
[형] [동] (관심을) 사로잡다, 붙다
번역:
Only a small number of adults engage in regular reading.

의미: crisis
예문:
[형] [명] 위기
번역:
economic crisis in 1997

의미: settle
예문:
[형] [동] 정착하다, (분쟁)가라앉히다
번역:
We need to learn how to settle an argument when it feels like you'll never agree.

의미: aid
예문:
[형] [명] 도움, 지원
번역:
The billionaire has pledged to donate $100 million dollars in humanitarian aid.

의미: delay
예문:
[형] [명] 지연
번역:
Heavy traffic causes delays on roads.

의미: insurance
예문:
[형] [명] 보험
번역:
I should file an insurance claim.

의미: length
예문:
[형] [명] 길이, 기간
번역:
We have to cut the length of the book by 20%.

의미: investigation
예문:
[형] [명] 수사, 조사
번역:
Criminal Scene Investigation (CSI)

의미: somewhere
예문:
[형] [명] 어딘가
번역:
somewhere over the rainbow

의미: expand
예문:
[형] [동] 확장되다, 확장시키다
번역:
Water expands as it freezes.

의미: commit
예문:
[형] [동] (범죄) 저지르다
번역:
The rate of crime committed by youth has been generally declining.

의미: weapon
예문:
[형] [명] 무기
번역:
North Korea is thought to be developing nuclear weapons.

의미: district
예문:
[형] [명] 지역
번역:
The largest slum district is Orangi Town in Pakistan.

의미: tire
예문:
[형] [동] 피곤하게 하다
번역:
I feel sleepy rather than tired.

의미: spirit
예문:
[형] [명] 정신, 영혼
번역:
I am 72, but I still feel young in spirit.

의미: pool
예문:
[형] [명] 물웅덩이, 수영장
번역:
Do you know where the swimming pool is?

의미: hardly
예문:
[형] [부] 거의 ~않다
번역:
I can hardly believe in God.

의미: award
예문:
[형] [명] 상, 상패, 상금
번역:
Parasite has won four Academy Awards.

의미: experiment
예문:
[형] [명] 실험
번역:
Ebbinghaus conducted experiments on memory retention.

의미: strange
예문:
[형] [형] 이상한, 낯선
번역:
It's strange that he never drinks beer.

의미: revenue
예문:
[형] [명] 수익
번역:
Apple's annual revenue rose by 45%.

의미: enable
예문:
[형] [동] ~할 수 있게 하다
번역:
The loan enabled Sue to buy an apartment.

의미: cancer
예문:
[형] [명] 암
번역:
My father died of pancreatic cancer.

의미: convince
예문:
[형] [동] 설득하다
번역:
Her opinion is not convincing at all.

의미: healthy
예문:
[형] [형] 건강한, 몸에 좋은
번역:
A fat tax is a tax on foods or drinks considered unhealthy.

의미: blow
예문:
[형] [동] (입으로, 바람이) 불다
번역:
She blew the smoke right in my face.

의미: location
예문:
[형] [명] 위치
번역:
My apartment is in a good location.

의미: opposite
예문:
[형] [형] 반대의
번역:
He turned and walked off in the opposite direction.

의미: sum
예문:
[형] [명] 금액, 합계
번역:
I got paid a modest sum for translation.

의미: murder
예문:
[형] [명] 살인
번역:
the evidence of his being a murderer

의미: soldier
예문:
[형] [명] 군인
번역:
soldiers who have served their country

의미: financial
예문:
[형] [형] 금융의, 재정의
번역:
FinTech is the abbreviation for financial technology.

의미: comfortable
예문:
[형] [형] 편안한
번역:
The Aeron chair is the most comfortable office chair!

의미: pack
예문:
[형] [동] 짐을 싸다, 포장하다
번역:
I forgot to pack my toothbrush.

의미: recall
예문:
[형] [동] 기억해내다
번역:
I can't recall the brand of this chair.

의미: manufacture
예문:
[형] [동] 제조하다
번역:
Ford Motor Company manufactures vehicles.

의미: theater
예문:
[형] [명] 극장
번역:
We haven't been to the theater for a year.

의미: freedom
예문:
[형] [명] 자유
번역:
the freedom of the press

의미: dear
예문:
[형] [형] 친한, 애정어린
번역:
Kyummo became a dear friend of mine when I was a teenager.

의미: objective
예문:
[형] [형] 객관적인
번역:
I'd like an objective opinion.

의미: moreover
예문:
[형] [부] 더욱이
번역:
The price of the new iPhone is too high and, moreover, it is sold-out.

의미: branch
예문:
[형] [명] 나뭇가지, 지점
번역:
A bird sitting on a tree is never afraid of the branch breaking.

의미: bind
예문:
[형] [동] 묶다
번역:
The pile of magazines was bound with string.

의미: belong
예문:
[형] [동] ~에 속하다
번역:
Take me home to the place I belong.

의미: army
예문:
[형] [명] 군대
번역:
I joined the army right after I graduated from university.

의미: decrease
예문:
[형] [명] 감소, 하락
번역:
a decrease in demand and an increase in supply

의미: hurt
예문:
[형] [동] 다치다, 상처를 주다
번역:
My knees hurt after running, but not during.

의미: council
예문:
[형] [명] 의회
번역:
A council is a group of people who come together to consult, deliberate, or make decisions.

의미: sight
예문:
[형] [명] 시력, 시야
번역:
My sight is poor for someone of my age.

의미: generate
예문:
[형] [동] 발생시키다
번역:
How much electricity does an electric eel generate?

의미: deny
예문:
[형] [동] 부인하다
번역:
I can't deny that I dislike white chocolate.

의미: quote
예문:
[형] [명] 인용구
번역:
One of my favorite quotes is: "the limits of my language are the limits of my world."

의미: violence
예문:
[형] [명] 폭력
번역:
She was a victim of domestic violence.

의미: minister
예문:
[형] [명] 장관, 성직자
번역:
The Minister of National Defense is 정경두.

의미: noise
예문:
[형] [명] 소음
번역:
There was a strange noise in my ears.

의미: occasion
예문:
[형] [명] 경우, 때
번역:
He saved a bottle of champagne for a special occasion.

의미: familiar
예문:
[형] [형] 익숙한
번역:
Are you familiar with Lumafusion?

의미: ignore
예문:
[형] [동] 무시하다
번역:
I sometimes ignore phone calls.

의미: destroy
예문:
[형] [동] 파괴하다
번역:
The factory was completely destroyed by fire.

의미: affair
예문:
[형] [명] 일, 사건
번역:
We should pay attention to world affairs.

의미: civil
예문:
[형] [형] 시민의
번역:
Civil rights include the ensuring of people's integrity, life, and safety.

의미: citizen
예문:
[형] [명] 시민, 주민
번역:
The government needs to take care of its citizens.

의미: temperature
예문:
[형] [명] 온도, 체온
번역:
The nurse took my temperature.

의미: domestic
예문:
[형] [형] 국내의, 가정의
번역:
She was a victim of domestic violence.

의미: load
예문:
[형] [명] 많은 (짐, 업무) 양
번역:
My workload is too heavy.

의미: troop
예문:
[형] [명] 병력, 군대
번역:
troops dispatched to Iraq

의미: remind
예문:
[형] [동] 상기시키다, 생각나게 하다
번역:
Oh, that reminds me, I must buy soap.

의미: prison
예문:
[형] [명] 감옥
번역:
고유정 went to prison for murder.

의미: acquire
예문:
[형] [동] 얻다, 습득하다
번역:
How can I acquire supernatural powers?

의미: participate
예문:
[형] [동] 참여하다
번역:
How important is it for students to actively participate in class discussions?

의미: tear
예문:
[형] [명] 눈물
번역:
Watching the movie, I tried to fight back tears.

의미: capacity
예문:
[형] [명] 용량, 능력
번역:
The fuel tank has a capacity of 50 liters.

의미: border
예문:
[형] [명] 경계, 국경
번역:
You need a valid passport to cross the border.

의미: fee
예문:
[형] [명] 요금, 수수료
번역:
The museum charges an entrance fee.

의미: regulation
예문:
[형] [명] 규정, 규제
번역:
There are new regulations on YouTube that will come into effect on January 1.

의미: escape
예문:
[형] [동] 탈출하다, 벗어나다
번역:
No one can escape from death.

의미: proper
예문:
[형] [형] 적절한
번역:
Do you know the proper way to clean the teeth?

의미: component
예문:
[형] [명] 구성 요소
번역:
What are the key components of a computer?

의미: afford
예문:
[형] [동] ~할 여유가 있다
번역:
I can't afford to buy a BMW.

의미: lawyer
예문:
[형] [명] 변호사
번역:
The murderer hired a very expensive lawyer.

의미: suspect
예문:
[형] [동] 의심하다
번역:
She is suspected of murder.

의미: confidence
예문:
[형] [명] 자신감
번역:
I didn't have any confidence in myself.

의미: complain
예문:
[형] [동] 불평하다
번역:
You can complain, but I doubt if it will make any difference.

의미: perspective
예문:
[형] [명] 견해, 관점
번역:
a whole new perspective on life

의미: arrest
예문:
[형] [동] 체포하다
번역:
He was arrested for fraud.

의미: assess
예문:
[형] [동] 평가하다
번역:
assess the value of a company

의미: asset
예문:
[형] [명] 자산, 재산
번역:
I transferred all my assets into my wife's name.

의미: absorb
예문:
[형] [동] 흡수하다, 빨아들이다
번역:
Plants absorb nutrients from the soil.

의미: relevant
예문:
[형] [형] 관련있는
번역:
My major is not relevant to my job.

의미: explore
예문:
[형] [동] 탐험하다, 조사하다
번역:
The rover will explore Mars in 2020.

의미: bond
예문:
[형] [명] 유대, 접착
번역:
A maternal bond is the relationship between a mother and her child.

의미: hire
예문:
[형] [동] 고용하다
번역:
The murderer hired a very expensive lawyer.

의미: tie
예문:
[형] [동] 묶다
번역:
Tie your shoelaces.

의미: internal
예문:
[형] [형] 내부의
번역:
conduct an internal audit

의미: literature
예문:
[형] [명] 문학
번역:
I need to read the major works of literature.

의미: victim
예문:
[형] [명] 피해자
번역:
She was a victim of domestic violence.

의미: threaten
예문:
[형] [동] 위협하다
번역:
Poaching threatens the survival of endangered animals.

의미: division
예문:
[형] [명] 분할, 나눗셈
번역:
achieve a fair division of wealth among the members of society

의미: accelerate
예문:
[형] [동] 속도를 내다
번역:
If you drop an object, it will accelerate downward at a rate of 9.8 m/s/s. 

의미: amaze
예문:
[형] [동] 놀라게 하다
번역:
If you could live forever, it would be amazing.

의미: device
예문:
[형] [명] 장치, 기구
번역:
The vacuum cleaner is a labor-saving device.

의미: label
예문:
[형] [명] 표, 상표
번역:
It says "Do NOT wash" on the label.

의미: expense
예문:
[형] [명] 비용
번역:
pay for my father's medical expenses

의미: typical
예문:
[형] [형] 전형적인
번역:
a typical example of a cv

의미: friendly
예문:
[형] [형] 친절한, 다정한
번역:
The staff were all very friendly.

의미: resident
예문:
[형] [명] 거주자
번역:
This event is exclusively for the residents of Yangju.

의미: concentrate
예문:
[형] [동] 집중하다
번역:
I can't concentrate on studying.

의미: accumulate
예문:
[형] [동] 축적하다, 쌓다
번역:
accumulate wealth and power

의미: plenty
예문:
[형] [대] 풍부한 양
번역:
I've got plenty of time.

의미: export
예문:
[형] [동] 수출하다
번역:
Korea exports semiconductors to many countries.

의미: consist
예문:
[형] [동] ~로 구성되다
번역:
The team consists of several experts in physics.

의미: graduate
예문:
[형] [동] 졸업하다
번역:
I joined the army right after I graduated from university.

의미: moral
예문:
[형] [형] 도덕적인
번역:
Keeping a promise is a moral issue.

의미: insist
예문:
[형] [동] 주장하다, 고집하다
번역:
Stay for supper, I insist.

의미: abuse
예문:
[형] [명] 남용, 학대
번역:
Prescription drug abuse is illegal.

의미: principal
예문:
[형] [명] 교장
번역:
I don't know the principal of the school.

의미: definitely
예문:
[형] [부] 확실히, 분명히
번역:
My wife definitely needs a holiday.

의미: session
예문:
[형] [명] (특정 활동의) 기간, 수업
번역:
Q&A session will follow after the presentation.

의미: grade
예문:
[형] [명] 학년
번역:
My daughter is in first grade.

의미: nevertheless
예문:
[형] [부] 그럼에도 불구하고
번역:
Scientists insist afterlife is impossible. Many people, nevertheless, believe life after death.

의미: predict
예문:
[형] [동] 예측하다, 예보하다
번역:
We can't predict the future.

의미: acid
예문:
[형] [명] 산, 산성
번역:
Lysergic acid diethylamide (LSD) is a hallucinogenic drug.

의미: rent
예문:
[형] [동] 임대하다
번역:
I'd rather rent a house than buy one.

의미: guarantee
예문:
[형] [동] 보장하다
번역:
I can't guarantee that I am always right.

의미: odd
예문:
[형] [형] 이상한, 홀수의
번역:
Odd numbers can't be divided exactly by two.

의미: approve
예문:
[형] [동] 승인하다, 찬성하다
번역:
I don't approve of any form of violence.

의미: loan
예문:
[형] [명] 대출, 융자
번역:
I'd like to apply for a small business loan.

의미: atmosphere
예문:
[형] [명] 대기, 분위기
번역:
The pub has an odd atmosphere, doesn't it?

의미: actually
예문:
[형] [부] 실제로
번역:
How often do airline blankets actually get washed?

의미: license
예문:
[형] [명] 면허, 인가
번역:
In order to sell alcohol, a restaurant has to get the license.

의미: rely
예문:
[형] [동] 의지하다, 믿다
번역:
Most children rely on their parents.

의미: permit
예문:
[형] [동] 허가하다
번역:
I wish smoking was not permitted in the apartments.

의미: wild
예문:
[형] [명] 야생
번역:
The birds are eventually released into the wild.

의미: commission
예문:
[형] [명] 판매 수수료
번역:
The agent takes a 10% commission on the sales she makes.

의미: unique
예문:
[형] [형] 독특한, 유일한
번역:
Jeju Island has a unique dialect.

의미: instrument
예문:
[형] [명] 도구, 악기
번역:
Do you play any musical instrument?

의미: acute
예문:
[형] [형] 극심한, 예리한
번역:
For no particular reason, she felt acute pain in her neck. 

의미: row
예문:
[형] [명] 줄, 열
번역:
I want to sit in the front row.

의미: youth
예문:
[형] [명] 젊음, 청년
번역:
The rate of crime committed by youth has been generally declining.

의미: lock
예문:
[형] [동] (자물쇠로) 잠그다
번역:
Did you lock the door?

의미: fuel
예문:
[형] [명] 연료
번역:
Hybrid vehicles use less fuel. 

의미: celebrate
예문:
[형] [동] 축하하다, 기념하다
번역:
Yesterday, we went out for a meal to celebrate my mother's birthday.

의미: sexual
예문:
[형] [형] 성적인
번역:
All sexual harassment and sexual assault must be taken seriously.

의미: shoulder
예문:
[형] [명] 어깨
번역:
standing on the shoulders of the giants

의미: breath
예문:
[형] [명] 호흡
번역:
I smelt beer on his breath.

의미: import
예문:
[형] [동] 수입하다
번역:
Korea imports oil from the Middle East.

의미: sheet
예문:
[형] [명] (종이)한 장
번역:
Can I have a sheet of paper?

의미: cast
예문:
[형] [동] (미소, 시선) 던지다
번역:
Recent studies cast new light on this problem.

의미: notion
예문:
[형] [명] 개념
번역:
the traditional notion of marriage

의미: journey
예문:
[형] [명] 여행
번역:
a journey across the world

의미: allocate
예문:
[형] [동] 할당하다
번역:
You should allocate the same amount of time to each question.

의미: relief
예문:
[형] [명] 안도, 완화
번역:
I laughed in relief.

의미: debt
예문:
[형] [명] 부채
번역:
I don't have enough money to pay off my debts.

의미: honor
예문:
[형] [명] 존경, 영광, 명예
번역:
It is my honor to be with you tonight.

의미: outcome
예문:
[형] [명] 결과
번역:
For my family, the keyword in 2020 was outcome.

의미: blame
예문:
[형] [동] 비난하다, 탓하다
번역:
I blamed her mother. Her mother did everything for her.

의미: recover
예문:
[형] [동] 회복하다
번역:
I've recovered from my cold.

의미: stretch
예문:
[형] [동] 늘어나다, 뻗다
번역:
A rubber band can be stretched.

의미: declare
예문:
[형] [동] 선언하다
번역:
The Korean government has declared that the epidemic has reached 'community-level outbreak' stage.

의미: retire
예문:
[형] [동] 은퇴하다
번역:
Most people retire before 70.

의미: tiny
예문:
[형] [형] 아주 작은
번역:
a tiny little baby

의미: suitable
예문:
[형] [형] 적합한
번역:
I am hoping to find a suitable job.

의미: native
예문:
[형] [형] 토박이의, 태어난
번역:
English is not the native language for Koreans.

의미: analyze
예문:
[형] [동] 분석하다
번역:
It is not easy to analyze the results of the survey.

의미: artificial
예문:
[형] [형] 인공적인
번역:
I'd buy an artificial fur coat, rather than a genuine one.

의미: witness
예문:
[형] [명] 목격자
번역:
The police have appealed for witnesses to come forward.

의미: terrible
예문:
[형] [형] 끔직한, 형편없는
번역:
No one would buy the laptop because it is in a terrible state.

의미: ordinary
예문:
[형] [형] 일상적인, 보통의
번역:
This book is written in ordinary language.

의미: entry
예문:
[형] [명] 입장, 출입
번역:
Entry is free for children under three.

의미: fellow
예문:
[형] [형] 동료의 
번역:
He is my fellow researcher.

의미: chemical
예문:
[형] [형] 화학의
번역:
Helium is a chemical element with the symbol He.

의미: capture
예문:
[형] [동] 붙잡다
번역:
Pressing the key Print Screen captures an image of your entire screen.

의미: discount
예문:
[형] [명] 할인
번역:
You get a discount if you buy more than 10 pieces.

의미: peak
예문:
[형] [명] 산꼭대기, 절정
번역:
Most UFC fighters reach their peak in their mid-20s.

의미: bitter
예문:
[형] [형] (억울해서) 쓰라린, 쓴
번역:
Tom felt very bitter about him having bought a house.

의미: shout
예문:
[형] [동] 소리치다
번역:
"Watch out!" he shouted.

의미: yard
예문:
[형] [명] 마당
번역:
My kids are playing in the back yard.

의미: constant
예문:
[형] [형] 끊임없는, 변치않는
번역:
Constant practice is the only way to learn a foreign language.

의미: instruction
예문:
[형] [명] 설명, 지시
번역:
We need very specific instructions.

의미: intelligence
예문:
[형] [명] 지능
번역:
AI means artificial intelligence.

의미: ideal
예문:
[형] [형] 이상적인
번역:
What is your ideal type of woman?

의미: folk
예문:
[형] [명] 사람들
번역:
ordinary folks

의미: somewhat
예문:
[형] [부] 어느 정도
번역:
The price is somewhat cheaper than I expected.

의미: blank
예문:
[형] [명] 빈칸, 여백
번역:
Please fill in the blanks.

의미: poll
예문:
[형] [명] 투표, 여론 조사
번역:
a public opinion poll

의미: weak
예문:
[형] [형] 약한
번역:
I have a weak stomach.

의미: faith
예문:
[형] [명] 믿음, 신념
번역:
a little bit of faith

의미: reserve
예문:
[형] [동] 예약하다
번역:
I'd like to reserve a table for four.

의미: bored
예문:
[형] [형] 지루해진
번역:
This movie made me feel bored.

의미: somehow
예문:
[형] [부] 어떻게든
번역:
Somehow, I managed to escape from the room.

의미: passenger
예문:
[형] [명] 승객
번역:
Neither the pilot nor the passengers has died.

의미: justice
예문:
[형] [명] 정의
번역:
Justice always wins in the end.

의미: phase
예문:
[형] [명] 단계
번역:
This project is in the initial phase.

의미: thin
예문:
[형] [형] 얇은, 여윈
번역:
Roads are covered with a thin layer of ice. 

의미: rush
예문:
[형] [동] 돌진하다
번역:
We shouldn't rush to the conclusion.

의미: formal
예문:
[형] [형] 공식적인, 격식을 차린
번역:
Following several days of speculation, a formal announcement was made.

의미: religion
예문:
[형] [명] 종교, 신앙
번역:
freedom of religion

의미: calm
예문:
[형] [형] 고요한, 평온한
번역:
Please remain calm and evacuate the building immediately.

의미: reject
예문:
[형] [동] 거부하다, 거절하다
번역:
My job application has been rejected.

의미: plate
예문:
[형] [명] 접시
번역:
a pile of plates

의미: ban
예문:
[형] [명] 금지
번역:
a complete ban on smoking 

의미: steal
예문:
[형] [동] 훔치다
번역:
He stole money from his classmates.

의미: protest
예문:
[형] [명] 항의, 시위
번역:
Irish-based British people are planning to hold a protest against Brexit.

의미: frequently
예문:
[형] [부] 자주, 흔히
번역:
I frequently eat chicken.

의미: command
예문:
[형] [동] 명령, 지휘
번역:
The soldiers massacred more than 100 civilians under the general's command.

의미: impression
예문:
[형] [명] 인상
번역:
When we met the actor, we got a very good impression on him.

의미: column
예문:
[형] [명] 기둥, 칼럼
번역:
The Parthenon had 46 outer columns and 23 inner columns in total.

의미: candidate
예문:
[형] [명] 후보
번역:
Ahn endorsed the candidate.

의미: electronic
예문:
[형] [형] 전자의
번역:
an electronic guitar

의미: impose
예문:
[형] [동] 부과하다
번역:
It seems reasonable to impose tax on alcohol.

의미: ancient
예문:
[형] [형] 고대의
번역:
the Seven Wonders of the Ancient World

의미: coast
예문:
[형] [명] 해안
번역:
drive down the east coast of Korea

의미: ill
예문:
[형] [형] 아픈, 병든
번역:
He is terminally ill with cancer.

의미: multiple
예문:
[형] [형] 복수의, 다수의
번역:
A paragraph consists of multiple sentences.

의미: yield
예문:
[형] [동] (결과, 농작물) 내다
번역:
My work will yield meaningful outcome this year.

의미: legislation
예문:
[형] [명] 제정된 법
번역:
EU legislation on immigration and asylum is based on EU Treaty rights of free movement. 

의미: assistant
예문:
[형] [명] 조수, 점원
번역:
The personal digital assistant (PDA) is an old version of the smartphone.

의미: implement
예문:
[형] [동] 실행하다
번역:
implement a plan

의미: attach
예문:
[형] [동] 붙이다, 첨부하다
번역:
Attach your ID photo to your application.

의미: curiosity
예문:
[형] [명] 호기심
번역:
Out of curiosity, Dorothy followed the yellow brick road.

의미: everywhere
예문:
[형] [부] 어디에나, 모든 곳에
번역:
God is everywhere.

의미: household
예문:
[형] [형] 가정의
번역:
Sharing household chores helps prevent marital conflict.

의미: acknowledge
예문:
[형] [동] 인정하다
번역:
She acknowledged that she was angry.

의미: reward
예문:
[형] [명] 보상
번역:
Many schools have a system of rewards and punishments to encourage good behavior.

의미: academic
예문:
[형] [형] 학업의
번역:
his performance in academic work

의미: meanwhile
예문:
[형] [부] 그 동안에
번역:
Her son was in the library. She, meanwhile, went back home and did some household chores.

의미: furthermore
예문:
[형] [부] 더욱이, 게다가
번역:
The coronavirus has spread, and furthermore, the level of fine dust in the air has increased.

의미: accuse
예문:
[형] [동] 고발하다, 비난하다
번역:
고유정 is accused of murder.

의미: wage
예문:
[형] [명] 임금
번역:
a weekly wage of $300

의미: absence
예문:
[형] [명] 결석, 부재
번역:
In the absence of any evidence, people wouldn't believe in God.

의미: construct
예문:
[형] [동] 건설하다, 구성하다
번역:
an apartment to be constructed this year

의미: remark
예문:
[형] [명] 발언
번역:
my boss's introductory remarks

의미: customize 
예문:
[형] [동] (원하는대로) 주문 제작하다
번역:
Many women enrolled in customized sessions for losing weight. 

의미: rare
예문:
[형] [형] 드문
번역:
a rare opportunity to meet celebrities 

의미: intention
예문:
[형] [명] 의도
번역:
I had no intention of offence.

의미: dozen
예문:
[형] [명] 12개 묶음
번역:
Dozens of civilians were injured in the accident.

의미: minimum
예문:
[형] [명] 최소
번역:
What is the minimum requirements for the job?

의미: real estate
예문:
[형] [명] 부동산
번역:
a licensed real estate agent

의미: expose
예문:
[형] [동] 노출시키다, 폭로하다
번역:
Julian Assange exposed truth as a journalist, said his lawyer.

의미: shut
예문:
[형] [동] 닫다
번역:
Shut down the door.

의미: resolve
예문:
[형] [동] 해결하다, 결심하다
번역:
Marital conflicts can be resolved, maybe, by sharing household chores.

의미: enormous
예문:
[형] [형] 거대한
번역:
An enormous exhibition hall is being built in the middle of Seoul. 

의미: permanent
예문:
[형] [형] 영구적인
번역:
He wants to get a stable, permanent job. 

의미: diagnose
예문:
[형] [동] (병, 문제) 진단하다
번역:
My father was diagnosed with pancreatic cancer.

의미: emotion
예문:
[형] [명] 감정
번역:
Anger is a waste of emotion.

의미: pursue
예문:
[형] [동] 추구하다
번역:
It is very important to pursue your own interest.

의미: urge
예문:
[형] [동] 촉구하다, 재촉하다
번역:
Sometimes, my wife urges me to do things that make a lot of money.

의미: enemy
예문:
[형] [명] 적, 적군
번역:
Who is your enemy?

의미: appoint
예문:
[형] [동] 임명하다, 정하다
번역:
The president promised to appoint more women to senior positions.

의미: talent
예문:
[형] [명] 재능
번역:
He has a lot of talent.

의미: priority
예문:
[형] [명] 우선 사항
번역:
I need to get my priorities straight.

의미: phrase
예문:
[형] [명] 구, 구절
번역:
His conversation is full of colorful phrases.

의미: pilot
예문:
[형] [명] 조종사
번역:
Neither the pilot nor the passengers has died.

의미: stable
예문:
[형] [형] 안정된
번역:
He wants to get a stable, permanent job. 

의미: merely
예문:
[형] [부] 단지, 그저
번역:
We're merely good friends.

의미: resolution
예문:
[형] [명] 결의안, 합의안
번역:
The resolution has been passed by a two-thirds majority.

의미: communicate
예문:
[형] [동] 의사소통하다
번역:
I communicate mostly by email.

의미: injury
예문:
[형] [명] 부상
번역:
The UFC fighter got a nasty facial injury in the bout.

의미: vast
예문:
[형] [형] 광대한
번역:
In the photo, the man stood in a vast desert.

의미: fasten
예문:
[형] [동] 매다, 채우다
번역:
Please, fasten your seatbelts.

의미: exhibition
예문:
[형] [명] 전시, 전시회
번역:
An enormous exhibition hall is being built in the middle of Seoul. 

의미: incident
예문:
[형] [명] 사건
번역:
His plane arrived without incident.

의미: childhood
예문:
[형] [명] 어린 시절
번역:
My childhood was fairly normal.

의미: draft
예문:
[형] [명] 초고, 초안
번역:
You have to finish your first draft as quickly as possible.

의미: slip
예문:
[형] [동] 미끄러지다
번역:
She slipped on the ice.

의미: accompany
예문:
[형] [동] 동행하다
번역:
If you accompany Jane, she will be very happy.

의미: knock
예문:
[형] [동] 두드리다
번역:
knocking on heaven's door.

의미: seed
예문:
[형] [명] 씨, 근원
번역:
Plant the seeds two inches apart.

의미: illustrate
예문:
[형] [동] 명확하게 설명하다
번역:
To illustrate my point, I will give an example.

의미: imply
예문:
[형] [동] 암시하다, 내포하다
번역:
A price increase implies an increased demand.

의미: temporary
예문:
[형] [형] 임시의
번역:
Temporary tattoos last about three days.

의미: liberal
예문:
[형] [형] 개방적인, 자유주의의, 후한
번역:
liberal parents

의미: harvest
예문:
[형] [명] 추수, 수확
번역:
Farmers are expecting a good harvest this year.

의미: qualify
예문:
[형] [동] 자격을 주다
번역:
The NAATI certificate qualifies me to work as a professional translator.

의미: core
예문:
[형] [명] 중심부, 핵심
번역:
What is in the core of the earth?

의미: aircraft
예문:
[형] [명] 항공기
번역:
Choppers, jets and airplanes are the synonyms for aircraft.

의미: self
예문:
[형] [명] 자기, 자신
번역:
You have to believe in yourself.

의미: metal
예문:
[형] [명] 금속
번역:
The handle is made of metal.

의미: emphasize
예문:
[형] [동] 강조하다
번역:
The book emphasizes the importance of reading.

의미: maximum
예문:
[형] [형] 최대의
번역:
a maximum speed limit of in Korea

의미: hatred
예문:
[형] [명] 증오, 혐오
번역:
Some Koreans could feel hatred towards the Chinese due to coronavirus.

의미: elsewhere
예문:
[형] [부] 다른 어떤 곳에서
번역:
You should look elsewhere for the answer.

의미: bother
예문:
[형] [동] (귀찮게) 신경쓰이게 하다
번역:
I am sorry to bother you.

의미: motion
예문:
[형] [명] 운동, 동작
번역:
Newton's first law of motion

의미: gray
예문:
[형] [명] 회색
번역:
I like gray because it's in between black and white.

의미: complicate
예문:
[형] [동] 복잡하게 만들다
번역:
It makes things more complicated.

의미: discipline
예문:
[형] [명] 규율, 훈육
번역:
This book gives teachers advice on discipline.

의미: disappoint
예문:
[형] [동] 실망시키다
번역:
I was disappointed with the number of subscribers. 

의미: freeze
예문:
[형] [동] 얼다
번역:
I nearly froze to death last night.

의미: passage
예문:
[형] [명] 통로, (책의) 구절
번역:
My office is just along the passage.

의미: reputation
예문:
[형] [명] 명성
번역:
My YouTube channel will have a very good reputation.

의미: forth
예문:
[형] [부] 멀리 앞/바깥쪽으로
번역:
The soldier waved a flag back and forth.

의미: horizon
예문:
[형] [명] 시야, 수(지)평선
번역:
Read as many books as possible if you want to broaden your horizons.

의미: democracy
예문:
[형] [명] 민주주의
번역:
Simply, democracy means "rule by the people."

의미: crash
예문:
[형] [명] 충돌
번역:
It's very unusual that two planes crash in mid-air.

의미: implication
예문:
[형] [명] (현 행동이 초래할 수 있는) 결과, 영향
번역:
the social implications of smartphones

의미: deserve
예문:
[형] [동] ~할 가치가 있다
번역:
Take the prize. You deserve it.

의미: unusual
예문:
[형] [형] 보통이 아닌
번역:
It's very unusual that two planes crash in mid-air.

의미: interaction
예문:
[형] [명] 상호 작용
번역:
Price is determined through the interaction of demand and supply.

의미: repair
예문:
[형] [명] 수리
번역:
Where can I get my shoes repaired?

의미: collapse
예문:
[형] [동] 무너지다
번역:
This little red plastic chair collapsed under my weight.

의미: fundamental
예문:
[형] [형] 근본적인
번역:
the fundamental cause of the coronavirus

의미: instinct
예문:
[형] [명] 본능
번역:
Animals have a natural instinct for survival.

의미: abroad
예문:
[형] [부] 해외에
번역:
I never travelled abroad when I was a kid.

의미: soul
예문:
[형] [명] 영혼
번역:
I don't believe in the immortality of the soul.

의미: capable
예문:
[형] [형] ~할 능력/자격이 있는
번역:
My family is capable of living abroad.

의미: defeat
예문:
[형] [동] 이기다, 패배시키다
번역:
We defeated the opposing team by 2 points.

의미: perfectly
예문:
[형] [부] 완벽하게, 완전하게
번역:
What I have done is perfectly legal.

의미: enhance
예문:
[형] [동] (긍정적 부분을 더) 강화하다
번역:
We use big data to enhance our services.

의미: proud
예문:
[형] [형] 자랑스러운
번역:
I am very proud of you.

의미: emergency
예문:
[형] [명] 비상 사태, 위급 상황
번역:
In case of emergency, break the glass with this hammer.

의미: distinguish
예문:
[형] [동] 구별하다
번역:
Students should have an ability to distinguish between fact and opinion. 

의미: substantial
예문:
[형] [형] (양, 숫자) 상당히 큰
번역:
They spent a substantial amount of money just for a day.

의미: nearby
예문:
[형] [형] 근처의
번역:
When you find a lost wallet, return it to a nearby police station.

의미: slide
예문:
[형] [동] 미끄러지다
번역:
I slid out of the room when the teacher wasn't looking at me. 

의미: valuable
예문:
[형] [형] 가치있는, 값비싼
번역:
Don't leave valuable belongings unattended.

의미: breast
예문:
[형] [명] 가슴, 유방
번역:
John cradled the baby against his breast.

의미: cope
예문:
[형] [동] (문제에) 잘 대처하다
번역:
Everyone wants to know how to cope with coronavirus anxiety. 

의미: approximately
예문:
[형] [부] 대략
번역:
The airplane will be taking off in approximately ten minutes. 

의미: invade
예문:
[형] [동] (공격하여) 침략하다
번역:
The Western Allies invaded German-occupied France in 1944.

의미: accommodation
예문:
[형] [명] 숙박시설
번역:
This package includes flights, meals, and accommodation.

의미: climate
예문:
[형] [명] 기후
번역:
Korea's climate is hot and humid in summer.

의미: exception
예문:
[형] [명] 예외
번역:
Everyone must wear a mask; kids are no exception.

의미: corporation
예문:
[형] [명] (큰 규모의) 기업, 법인
번역:
Samsung Electronics is a multinational corporation.

의미: encounter
예문:
[형] [동] (우연히 문제나 저항을) 마주치다
번역:
The government has encountered strong opposition.

의미: excuse
예문:
[형] [명] 변명
번역:
There is no excuse for being late.

의미: urban
예문:
[형] [형] 도시의
번역:
The average house price in urban areas is far more expensive than rural areas.

의미: confuse
예문:
[형] [동] 혼란시키다
번역:
I always confuse you with your brother - you look so alike!

의미: output
예문:
[형] [명] 생산량
번역:
China's output of CO2

의미: likewise
예문:
[형] [부] 똑같이, 동일하게
번역:
I drew a bird and told my daughter to do likewise.

의미: massive
예문:
[형] [형] 거대한
번역:
Massive waves struck the region.

의미: install
예문:
[형] [동] 설치하다
번역:
Have you installed the app?

의미: calculate
예문:
[형] [동] 계산하다
번역:
Can we calculate the possibility of success?

의미: upper
예문:
[형] [형] 위에 있는
번역:
The upper class doesn't want the political system to change.

의미: occupy
예문:
[형] [동] (시간, 공간을) 차지하다
번역:
I need to pee, but the toilet is occupied.

의미: outline
예문:
[형] [명] 개요, 윤관
번역:
Let me sketch out the outline of the project.

의미: sufficient
예문:
[형] [형] (목적 달성에) 충분한
번역:
Face masks are not sufficient to prevent coronavirus.

의미: preserve
예문:
[형] [동] 보존하다, 보호하다
번역:
You can help to preserve the Amazon rainforest.

의미: split
예문:
[형] [동] 나뉘다, 분열되다
번역:
The war split Korea in two.

의미: swing
예문:
[형] [동] 흔들다, 휘두르다
번역:
Let your arms swing as you run.

의미: consistent
예문:
[형] [형] 일관된
번역:
Parents should be consistent in the way they treat their children.

의미: liver
예문:
[형] [명] 간
번역:
The largest solid internal organ is your liver.

의미: severe
예문:
[형] [형] 심각한, 가혹한
번역:
The earthquake caused severe damage to many buildings. 

의미: gene
예문:
[형] [명] 유전자
번역:
The number of human genes is about 20,000.

의미: prospect
예문:
[형] [명] (일이 일어날) 전망, 가능성
번역:
I see no prospect of things improving here.

의미: plot
예문:
[형] [명] 줄거리, 음모
번역:
The plot of Parasite is a bit confusing.

의미: integrate
예문:
[형] [동] 통합하다
번역:
integrate immigrants in society

의미: convention
예문:
[형] [명] 같은 분야 사람들의 모임, 관습
번역:
A handshake is a social convention.

의미: bet
예문:
[형] [동] 내기하다, 돈을 걸다
번역:
How much do you want to bet?

의미: retain
예문:
[형] [동] (기억 등) 유지하다, 보유하다
번역:
Your body retains water.

의미: sequence
예문:
[형] [명] 연속적인 순서
번역:
in a logical sequence

의미: plain
예문:
[형] [형] 명확하고, 평이한
번역:
We should speak in plain English.

의미: volunteer
예문:
[형] [명] 지원자, 자원봉사자
번역:
Most of the paperwork has been done by volunteers.

의미: lung
예문:
[형] [명] 폐
번역:
The study has confirmed that smoking can cause lung cancer.

의미: rural
예문:
[형] [형] 시골의
번역:
The average house price in urban areas is far more expensive than rural areas.

의미: abandon
예문:
[형] [동] 버리다, 포기하다
번역:
I had to abandon the car because it didn't start.

의미: silence
예문:
[형] [명] 고요, 침묵
번역:
I love the silence of space.

의미: rapidly
예문:
[형] [부] 빨리
번역:
Coronavirus is spreading rapidly over the world.

의미: efficient
예문:
[형] [형] 효율적인
번역:
What is an efficient way to memorize words?

의미: revolution
예문:
[형] [명] 혁명
번역:
There was an industrial revolution in Britain.

의미: delight
예문:
[형] [명] 기쁨
번역:
I screamed with delight when I won a doll at a claw machine.

의미: spell
예문:
[형] [동] 철자를 말하다
번역:
How do you spell "라이브러리?"

의미: premise
예문:
[형] [명] 전제
번역:
If the premise is true, then the conclusion tends to be true too.

의미: lean
예문:
[형] [동] (몸을)숙이다, 기대다
번역:
Lean the tile against the wall.

의미: dramatic
예문:
[형] [형] 급격한, 감격적인
번역:
the most dramatic fight in UFC history

의미: grateful
예문:
[형] [형] 고마워하는
번역:
I am so grateful for your help.

의미: protein
예문:
[형] [명] 단백질
번역:
There is a lot of protein in eggs.

의미: distribute
예문:
[형] [동] 분배하다, 유통하다
번역:
Face masks will be distributed among citizens.

의미: mop
예문:
[형] [동] (물기) 닦다
번역:
It was so hot that he had to keep mopping his face.

의미: derive
예문:
[형] [동] ~에서 비롯되다
번역:
Omega 3 is derived from fish oil.

의미: crucial
예문:
[형] [형] 중대한
번역:
The weather will be a crucial factor in tomorrow's game.

의미: unemployment
예문:
[형] [명] 실업, 실직
번역:
receive unemployment benefits

의미: crop
예문:
[형] [명] 농작물
번역:
The main crops in Korea are rice, barley, and beans.

의미: interpretation
예문:
[형] [명] 해석, 통역
번역:
One possible interpretation is that she wanted to marry him.

의미: landscape
예문:
[형] [명] 풍경
번역:
rural landscape in Korea

의미: fault
예문:
[형] [명] 잘못, 결함
번역:
It's my fault.

의미: minor
예문:
[형] [형] 덜 중요한
번역:
I have made some minor mistakes.

의미: storm
예문:
[형] [명] 폭풍
번역:
This is the worst storm since 1990.

의미: thick
예문:
[형] [형] 두꺼운
번역:
I wear thick glasses because of my poor eyesight.

의미: monopoly
예문:
[형] [명] 독점 
번역:
For years KT had a monopoly on telephone services in Korea.

의미: negotiate
예문:
[형] [동] 협상하다
번역:
The government refused to negotiate with the terrorist.

의미: dominate
예문:
[형] [동] 지배하다
번역:
The smartphone industry is dominated by two giant companies: Apple and Samsung.

의미: peer
예문:
[형] [명] 또래, 동료
번역:
Korean children do better in math than their peers in the US.

의미: pension
예문:
[형] [명] 연금, 생활 보조금
번역:
At what age can I start receiving my national pension?

의미: electricity
예문:
[형] [명] 전기
번역:
How much electricity does an electric eel generate?

의미: respectively
예문:
[형] [부] 각각
번역:
How much are these chocolate and candy? / They are $2 and $1 respectively.

의미: ultimately
예문:
[형] [부] 드디어, 마침내
번역:
Ultimately, he won a prize at the claw machine.

의미: proof
예문:
[형] [명] 증거
번역:
proof of the existence of God

의미: soil
예문:
[형] [명] 흙
번역:
soil retaining water

의미: niche
예문:
[형] [명] 틈새, 꼭 맞는 직업
번역:
I created a niche for myself in English education.

의미: upset
예문:
[형] [형] 화난, 속상한
번역:
I was deeply upset about the financial authentication certificate system.

의미: dispute
예문:
[형] [명] 논쟁, 분쟁
번역:
The professor got into a dispute over the tuition fee increase.

의미: entertainment
예문:
[형] [명] 오락, 여흥
번역:
Netflix provides endless entertainment with movies and TV shows.

의미: undertake
예문:
[형] [동] 착수하다
번역:
I undertook a project about an online English education.

의미: retail
예문:
[형] [명] 소매
번역:
I have a retail business plan.

의미: wire
예문:
[형] [명] 철사, 전선
번역:
This thin wire is for cutting boiled eggs.

의미: unlikely
예문:
[형] [형] ~할 것 같지 않은
번역:
He is unlikely to admit his crime.

의미: publication
예문:
[형] [명] 출판, 출판물
번역:
He spent March writing journals for publication

의미: organ
예문:
[형] [명] 장기
번역:
The largest solid internal organ is your liver.

의미: unknown
예문:
[형] [형] 미지의, 알 수 없는 
번역:
The deep sea remains almost entirely unknown.

의미: framework
예문:
[형] [명] 뼈대, 골조, 체계
번역:
This paper provides a framework for future research.

의미: zone
예문:
[형] [명] 구역, 지역
번역:
Tokyo is located in an earthquake zone.

의미: restrict
예문:
[형] [동] 제한하다
번역:
restrict the sale of gun

의미: trace
예문:
[형] [동] 찾다, 추적하다
번역:
Scientists are trying to trace the origin of life on earth.

의미: equivalent
예문:
[형] [형] 동등한, ~에 상당하는
번역:
a qualification which is equivalent to a BA degree

의미: solid
예문:
[형] [명] 고체
번역:
The solid form of water is known as ice.

의미: enterprise
예문:
[형] [명] 기업, 사업
번역:
KEPCO is a state-owned enterprise.

의미: elderly
예문:
[형] [형] (공손) 연세가 있는
번역:
a retirement village for the elderly

의미: owe
예문:
[형] [동] 빚지고 있다
번역:
She owes me twenty bucks.

의미: port
예문:
[형] [명] 항구
번역:
The ship is in port.

의미: pitch
예문:
[형] [동] (세게 조준해서) 던지다
번역:
I crumpled up the paper and pitched it into the bin.

의미: contemporary
예문:
[형] [형] 현대의
번역:
I don't understand contemporary art.

의미: register
예문:
[형] [동] (명단에) 등록하다, 신고하다
번역:
In Korea, parents have to register a birth within 30 days.

의미: specialist
예문:
[형] [명] 전문가
번역:
a specialist in negotiation

의미: assure
예문:
[형] [동] 보증하다, 안심시키다
번역:
The doctor assured me that my father would be fine.

의미: profile
예문:
[형] [명] 옆모습, 인물 소개
번역:
I love my wife's profile.

의미: crack
예문:
[형] [명] (갈라진) 금
번역:
My phone got a crack in the screen.

의미: numerous
예문:
[형] [형] 셀 수 없이 많은
번역:
Japanese brutalities are too numerous to mention.

의미: submit
예문:
[형] [동] 제출하다, 굴복하다
번역:
The company will pay for the training fee as long as we submit a report of what we learned.

의미: symptom
예문:
[형] [명] (병) 증상
번역:
What are the symptoms of coronavirus?

의미: virtually
예문:
[형] [부] 거의 사실과 같이
번역:
Virtually all the members of the Shincheonji Church were infected with coronavirus.

의미: era
예문:
[형] [명] 시대, 연대
번역:
How will the era of artificial intelligence transform society?

의미: coverage
예문:
[형] [명] 보도, 방송
번역:
live coverage of the match

의미: tension
예문:
[형] [명] 긴장, 팽팽함
번역:
Tension in the neck muscles can cause headaches.

의미: nervous
예문:
[형] [형] 긴장한, 불안한
번역:
Many people are nervous about coronavirus.

의미: input
예문:
[형] [명] 투입, 입력
번역:
"Garbage in, garbage out" is the concept that nonsense input data produces nonsense output.

의미: isolate
예문:
[형] [동] 고립시키다, 격리시키다
번역:
The village is isolated by the earthquake.

의미: eliminate
예문:
[형] [동] 제거하다
번역:
The smartphone is eliminating the need for the DSLR.

의미: prey
예문:
[형] [명] 먹이
번역:
The young deer are ideal prey for the lion.

의미: tight
예문:
[형] [형] 꽉 조이는, 단단한
번역:
The belt must be tight enough.

의미: secondary
예문:
[형] [형] 이차적인, 부수적인
번역:
secondary education

의미: welfare
예문:
[형] [명] 복지, 행복
번역:
child welfare in the third world

의미: recruit
예문:
[형] [동] 모집하다
번역:
It is getting difficult to recruit qualified workers.

의미: exclude
예문:
[형] [동] 제외하다
번역:
When they left, I felt excluded.

의미: string
예문:
[형] [명] 끈
번역:
The pile of magazines was bound with string.

의미: persuade
예문:
[형] [동] 설득하다
번역:
I finally managed to persuade my mom to have a medical checkup.

의미: inspire
예문:
[형] [동] 영감을 주다
번역:
I want to become someone who can inspire the young.

의미: grand
예문:
[형] [형] 웅장한, 위엄있는
번역:
The building looks grand and beautiful.

의미: hence
예문:
[형] [부] (앞에 나온) 그런 이유로
번역:
We can buy almost everything with money, hence money is important.

의미: crew
예문:
[형] [명] 승무원
번역:
a flight crew

의미: phenomenon
예문:
[형] [명] 현상
번역:
"YouTubers" is a new phenomenon.

의미: pupil
예문:
[형] [명] 학생
번역:
a first-grade pupil

의미: false
예문:
[형] [형] 사실이 아닌, 거짓의
번역:
The statement is either true or false.

의미: restore
예문:
[형] [동] (이전 상태로) 되돌리다
번역:
Fresh air in the forest will restore me to full health.

의미: formula
예문:
[형] [명] 공식, 방식
번역:
I perceived that there was no magic formula for success.

의미: proceed
예문:
[형] [동] 계속하다, 진행하다
번역:
After mopping his face, he proceeded to read the report.

의미: perceive
예문:
[형] [동] 인지하다
번역:
I perceived that there was no magic formula for success.

의미: sink
예문:
[형] [동] 가라앉다
번역:
Titanic sank in 1912.

의미: stare
예문:
[형] [동] 응시하다
번역:
What are you staring at?

의미: convert
예문:
[형] [동] 전환시키다
번역:
Steve Jobs converted a garage into an office.

의미: steady
예문:
[형] [형] 꾸준한
번역:
Slow and steady wins the race.

의미: sail
예문:
[형] [동] 항해하다
번역:
Columbus sailed to America.

의미: disaster
예문:
[형] [명] 재해, 재난
번역:
Coronavirus is not a natural disaster.

의미: pace
예문:
[형] [명] (걸음, 달리기) 속도
번역:
The average running pace for a sub-three-hour marathon is 4:15/km.

의미: devote
예문:
[형] [동] (시간, 노력) 쏟다
번역:
You should devote your time to English learning.

의미: resemble
예문:
[형] [동] 닮다
번역:
The format of Mr Trot resembles that of Miss Trot.

의미: vital
예문:
[형] [형] 매우 중요한, 활기찬
번역:
Police have found a vital clue.

의미: fascinate
예문:
[형] [동] 마음을 사로잡다
번역:
Quantum computing fascinated many of the scientists in the demonstration.

의미: external
예문:
[형] [형] 외부의
번역:
for external use only

의미: spare
예문:
[형] [형] 여분의
번역:
a spare key

의미: whenever
예문:
[형] [전] ~할 때마다
번역:
Whenever I smell fried chicken, I always want to eat some.

의미: depression
예문:
[형] [명] 우울증, 불경기
번역:
suffer from depression

의미: guilty
예문:
[형] [형] 죄를 범한, 죄책감이 드는
번역:
I feel really guilty about scolding my daughter.

의미: underlying
예문:
[형] [형] 근본적인, 밑에 깔린
번역:
the underlying problem of global warming

의미: incorporate
예문:
[형] [동] 포함시키다
번역:
Environmentally friendly features are incorporated into the building design.

의미: pour
예문:
[형] [동] 따르다, 쏟아지다
번역:
Pour water into a teapot.

의미: sweep
예문:
[형] [동] 쓸다, 휩쓸다
번역:
I swept the leaves off the garden.

의미: obligation
예문:
[형] [명] 의무, 책임
번역:
a moral obligation to help the poor

의미: sir
예문:
[형] [명] (남성) ~씨, ~님
번역:
Dear Sir or Madam,

의미: evaluate
예문:
[형] [동] 평가하다
번역:
Teachers should evaluate themselves continuously.

의미: pub
예문:
[형] [명] 술집
번역:
I don't really like to go to a pub. 

의미: ridiculous 
예문:
[형] [형] 터무니없는
번역:
It seems ridiculous to expect anyone to drive for four hours just for a five-minute meeting.

의미: perception
예문:
[형] [명] 자각, 통찰력
번역:
The public perception of the public schools has become tarnished over the past few decades.

의미: currency
예문:
[형] [명] 화폐
번역:
The euro is the single official currency of 19 of the 27 member states of the EU.

의미: territory
예문:
[형] [명] 영토, 영역
번역:
Hong Kong became Chinese territory in 1997.

의미: stream
예문:
[형] [명] 시냇물, 흐름
번역:
a stream of traffic

의미: height
예문:
[형] [명] 키, 고도
번역:
I am about the same height as my wife. 

의미: muscle
예문:
[형] [명] 근육
번역:
The Queen's Guard stood without moving a muscle.

의미: scare
예문:
[형] [동] 겁주다, 놀라게 하다
번역:
I moved quietly to avoid scaring the pigeons off.

의미: boundary
예문:
[형] [명] 경계, 한계
번역:
Anything that crosses the boundary of a black hole cannot get back.

의미: ratio
예문:
[형] [명] 비율
번역:
The ratio of alcohol to water is 4:3.

의미: scream
예문:
[형] [명] 비명
번역:
I heard a scream coming from the second floor.

의미: scatter
예문:
[형] [동] 흩뿌리다
번역:
The leaves fell and scattered on the ground.

의미: withdraw
예문:
[형] [동] 뒤로 빠지다, 중단하다
번역:
withdraw from the competition

의미: pollution
예문:
[형] [명] 오염, 공해
번역:
Beijing and Seoul have regular meetings about the air pollution from fine dust.

의미: disorder
예문:
[형] [명] 혼란, 장애
번역:
people with mental disorders

의미: furniture
예문:
[형] [명] 가구
번역:
He gave me some antique furniture.

의미: steel
예문:
[형] [명] 강철
번역:
stainless steel is steel that doesn't change color.

의미: transform
예문:
[형] [동] 변형시키다
번역:
How will the era of artificial intelligence transform society?

의미: wound
예문:
[형] [명] 부상, 상처
번역:
The doctor disinfected and sewed up the wound on my daughter's chin.

의미: foundation
예문:
[형] [명] 토대, 설립
번역:
It will take several months to lay the foundations of the apartments

의미: strain
예문:
[형] [명] 잡아당김, 스트레스
번역:
The strain on the cables supporting the bridge is enormous.

의미: shallow
예문:
[형] [형] 얕은, 얄팍한
번역:
Don't be fooled into thinking that shallow water is less risky than deeper water.

의미: trail
예문:
[형] [명] (발자국) 흔적, 오솔길
번역:
a trail of footprints in the snow

의미: trap
예문:
[형] [명] 덫, 가두는 것
번역:
Set a trap to catch mice.

의미: loose
예문:
[형] [형] 헐렁한, 느슨한
번역:
The screw became loose.

의미: wealth
예문:
[형] [명] 부, 재산
번역:
achieve a fair division of wealth among the members of society

의미: gradually
예문:
[형] [부] 서서히, 점차
번역:
Gradually, my knees have got worse.

의미: evil
예문:
[형] [명] 악, 악한 것
번역:
It is difficult to define good and evil using human criteria.

의미: tune
예문:
[형] [동] (악기, 채널) 조율, 조정하다
번역:
Stay tuned!

의미: transition
예문:
[형] [명] 변화, 전환
번역:
Korean society is now in transition.

의미: frighten
예문:
[형] [동] 겁먹게 하다
번역:
I was frightened by a sudden noise from the kitchen.

의미: bid
예문:
[형] [동] 값을 부르다, 입찰하다
번역:
Three companies bid for the contract on the subway construction.

의미: breed
예문:
[형] [동] (동물) 번식하다, 새끼 낳다
번역:
Many animals breed only at certain times of the year.

의미: extraordinary
예문:
[형] [형] 흔치 않은, 평범하지 않은
번역:
What an extraordinary chance to work with BTS!

의미: brilliant
예문:
[형] [형] 빛나는, 훌륭한
번역:
I think that's a brilliant idea.

의미: sphere
예문:
[형] [명] 구
번역:
A 3D version of a circle is a sphere.

의미: stem
예문:
[형] [명] (식물) 줄기
번역:
The rose's stem has many thorns.

의미: reverse
예문:
[형] [동] (반대로) 뒤집다, 바꾸다
번역:
reverse a decision

의미: awful
예문:
[형] [형] 끔찍한, (양적으로) 엄청난
번역:
If it is just us, it seems like an awful waste of space.

의미: adjust
예문:
[형] [동] 조절하다, 적응하다
번역:
Kids are good at adjusting.

의미: nowadays
예문:
[형] [부] 요즘에
번역:
Nowadays almost everyone has a smartphone.

의미: poem
예문:
[형] [명] 시
번역:
I wrote my wife a poem.

의미: planet
예문:
[형] [명] 행성
번역:
All the orbits of the planets in the solar system are oval rather than circular.

의미: knee
예문:
[형] [명] 무릎
번역:
My knees hurt after running, but not during.

의미: strand
예문:
[형] [명] 한 가닥, 올
번역:
I found a strand of hair in my soup.

의미: overcome
예문:
[형] [동] 극복하다
번역:
I was able to overcome fear of failure.

의미: depth
예문:
[형] [명] 깊이
번역:
the depth of the microwave

의미: entrance
예문:
[형] [명] 입구, 입장
번역:
The museum charges an entrance fee.

의미: portion
예문:
[형] [명] 부분, 분량
번역:
a substantial portion of the Korean population 

의미: substance
예문:
[형] [명] 물질, 본질, 요지
번역:
Plutonium is a toxic substance.

의미: extensive
예문:
[형] [형] 광범위한, 넓은
번역:
Extensive reading is one of useful ways to learn a foreign language.

의미: inner
예문:
[형] [형] 안쪽의, 내적인
번역:
The Parthenon had 46 outer columns and 23 inner columns in total.

의미: harm
예문:
[형] [명] 피해, 손해
번역:
It wouldn't do you any harm to listen to your parents.

의미: consult
예문:
[형] [동] 상담하다
번역:
A council is a group of people who come together to consult, deliberate, or make decisions.

의미: shadow
예문:
[형] [명] 그림자
번역:
walk in the shadow of the wall

의미: strip
예문:
[형] [동] (옷을) 벗다
번역:
The boys stripped naked and jumped in the sea.

의미: smooth
예문:
[형] [형] 매끄러운, 순조로운
번역:
My baby's skin feels smooth and warm.

의미: intervention
예문:
[형] [명] 중재, 간섭
번역:
government intervention in the stock market

의미: subtle
예문:
[형] [형] 미묘한, 감지하기 힘든
번역:
There are subtle differences between these two kinds of coffee beans.

의미: vice
예문:
[형] [명] 악덕, 비행
번역:
He has only one vice: overwork.

의미: radical
예문:
[형] [형] 근본적인, 급진적인
번역:
Korean churches need radical changes.

의미: loud
예문:
[형] [형, 부] 큰 소리의, 큰소리로
번역:
LOL means 'laugh out loud.'

의미: dimension
예문:
[형] [명] 치수, 차원
번역:
I want to know the exact dimensions of the room.

의미: subsequent
예문:
[형] [형] 그 이후의
번역:
These skills were passed on to subsequent generations

의미: infection
예문:
[형] [명] 감염
번역:
Travelers to China are being warned about the danger of coronavirus infection.

의미: statistics
예문:
[형] [명] 통계, 통계학
번역:
To make use of big data, many companies need experts in statistics.

의미: iron
예문:
[형] [명] 철, 다리미
번역:
He stood up and announced that he was Iron Man.

의미: broadcast
예문:
[형] [동] 방송하다
번역:
The boxing match was broadcast live all over the world.

의미: suicide
예문:
[형] [명] 자살
번역:
My opinion is that despair causes suicide.

의미: blind
예문:
[형] [형] 눈이 먼
번역:
guide dogs for the blind

의미: pure
예문:
[형] [형] 순수한, 깨끗한
번역:
24k means pure gold.

의미: ally
예문:
[형] [명] 동맹국, 연합국가들
번역:
The Western Allies invaded German-occupied France in 1944.

의미: quantity
예문:
[형] [명] 양
번역:
Big data literally means a vast quantity of data.

의미: bend
예문:
[형] [동] 굽히다, 구부리다
번역:
It is difficult to bend the steel.

의미: mature
예문:
[형] [형] 성숙한
번역:
Her son is very mature for his age.

의미: disturb
예문:
[형] [동] 방해하다
번역:
Sorry to disturb you, but …

의미: sustain
예문:
[형] [동] 유지하다
번역:
Eventually, the earth will be too hot to sustain life.

의미: flood
예문:
[형] [명] 홍수
번역:
A lack of vegetation can cause floods.

의미: poverty
예문:
[형] [명] 가난
번역:
Many people in North Korea live in poverty.

의미: cite
예문:
[형] [동] 인용하다, 예를 들다
번역:
It is essential to cite examples to support your argument.

의미: newly
예문:
[형] [부] 최근에, 새로이
번역:
Neologisms are newly coined words.

의미: parallel
예문:
[형] [형] 평행의
번역:
two parallel lines never meet.

의미: gender
예문:
[형] [명] 성, 성별
번역:
gender equality

의미: suspicion
예문:
[형] [명] 의심, 의혹
번역:
His arrogant attitude aroused my suspicion that he must be an asshole.

의미: accurate
예문:
[형] [형] 정확한
번역:
Sentences should be as accurate as possible. 

의미: burden
예문:
[형] [명] 부담
번역:
The burden of taxation falls more heavily on the poor.

의미: desert
예문:
[형] [명] 사막
번역:
In the photo, the man stood in a vast desert.

의미: mate
예문:
[형] [명] 짝궁, 친구
번역:
Most of my school mates are kind.

의미: shareholder
예문:
[형] [명] 주주
번역:
Larry Page is the top Google shareholder.

의미: tap
예문:
[형] [동] 톡톡치다
번역:
McGregor had no choice but to tap out.

의미: philosophy
예문:
[형] [명] 철학, 인생관
번역:
the philosophy of Aristotle

의미: attribute
예문:
[형] [동] 원인으로 보다
번역:
The government attributed the increase in coronavirus infection to Sincheonji Church.

의미: apologize
예문:
[형] [동] 사과하다
번역:
Her husband apologized to her for losing his temper.

의미: undermine
예문:
[형] [동] (기반) 약화시키다
번역:
The constant criticism couldn't undermine his confidence.

의미: grab
예문:
[형] [동] (확) 붙잡다
번역:
I grabbed my phone and ran off.

의미: entitle
예문:
[형] [동] 제목을 붙이다, 자격을 주다
번역:
You will be entitled to the national pension when you become 65.

의미: lend
예문:
[형] [동] 빌려주다
번역:
Could you lend me the beam-projector?

의미: translate
예문:
[형] [동] 번역하다
번역:
In order to translate English into Korean, you should know both of the languages well.

의미: deposit
예문:
[형] [명] 예금, 보증금
번역:
A deposit of 30% is required to buy the car.

의미: overseas
예문:
[형] [부] 해외로
번역:
I was studying overseas in 2008.

의미: advocate
예문:
[형] [동] 지지하다, 옹호하다
번역:
The teacher publicly advocated the use of violence.

의미: rough
예문:
[형] [형] 거친, 대략의
번역:
The surface of sandpaper is very rough.

의미: unify
예문:
[형] [동] 통합, 통일하다
번역:
If the two Koreas unify…

의미: seal
예문:
[형] [동] 봉인하다
번역:
The door was sealed with tape.

의미: spin
예문:
[형] [동] 돌다, 돌리다
번역:
If the earth is spinning, why can't we feel it?

의미: infant
예문:
[형] [명] 유아, 영아
번역:
An infant's skin is very smooth.

의미: dig
예문:
[형] [동] (땅을) 파다
번역:
There are several different reasons why a dog will dig.

의미: drag
예문:
[형] [동] 끌다
번역:
In order to remove the file, drag and drop it to the waste bin icon.

의미: mount
예문:
[형] [동] (이벤트) 개시하다, 올려두다
번역:
Hasajon English will soon mount the online writing course.

의미: wrap
예문:
[형] [동] 포장하다
번역:
She wrapped all of the gifts by herself.

의미: anticipate
예문:
[형] [동] 예상하다, 기대하다
번역:
The result was better than anticipated.

의미: anxiety
예문:
[형] [명] 걱정, 불안
번역:
Everyone wants to know how to cope with coronavirus anxiety. 

의미: precisely
예문:
[형] [부] 정확히
번역:
Laser can cut metal precisely.

의미: utilize
예문:
[형] [동] 활용하다, 이용하다
번역:
We must consider how best to utilize resources we have.

의미: offense
예문:
[형] [명] 공격, 범죄
번역:
No offense but…

의미: detect
예문:
[형] [동] 찾아내다, 감지하다
번역:
A nuclear launch is detected.

의미: teenager
예문:
[형] [명] 십대
번역:
Kyummo became a dear friend of mine when I was a teenager.

의미: admire
예문:
[형] [동] 존경하다
번역:
I really admire Steve Jobs.

의미: moderate
예문:
[형] [형] 중간의, 적당한
번역:
a moderate degree of heat 

의미: surgery
예문:
[형] [명] 수술
번역:
My knees may need surgery.

의미: illegal
예문:
[형] [형] 불법의
번역:
Prescription drug abuse is illegal.

의미: charity
예문:
[형] [명] 자선 단체
번역:
charity events

의미: constitute
예문:
[형] [동] (법) 성립하다, 되다
번역:
Over speeding constitutes an illegal act.

의미: adequate
예문:
[형] [형] 적절한
번역:
I don't believe that face masks are adequate now.

의미: vague
예문:
[형] [형] 희미한, 모호한
번역:
Only a vague outline of the measures was shown to the citizens.

의미: stupid
예문:
[형] [형] 어리석은
번역:
What is the most stupid mistake you've ever made?

의미: keen
예문:
[형] [형] ~을 열망하는
번역:
I am keen on going to the library.

의미: ethnic
예문:
[형] [형] 민족의
번역:
people from different ethnic groups

의미: twin
예문:
[형] [명] 쌍둥이
번역:
The twin buildings were the targets for the terrorists.

의미: clinical
예문:
[형] [형] 임상의
번역:
A new drug is undergoing clinical trials.

의미: forecast
예문:
[형] [명] 예보, 예측
번역:
Scientists have produced a pessimistic forecast on the spread of the virus.

의미: segment
예문:
[형] [명] 부분, 조각
번역:
an orange segment

의미: adapt
예문:
[형] [동] 적응하다
번역:
In March, children need to adapt to their new schools.

의미: prompt
예문:
[형] [형] 신속한, 즉각적인
번역:
Prompt action must be taken.

의미: charm
예문:
[형] [명] 매력
번역:
I like Sia because of her boyish charm.

의미: react
예문:
[형] [동] 반응하다
번역:
He reacted very badly when he came across the police officer.

의미: lecture
예문:
[형] [명] 강의
번역:
Many students find it difficult to listen to online lectures.

의미: compound
예문:
[형] [명] 혼합물
번역:
Water is a compound of hydrogen and oxygen.

의미: rescue
예문:
[형] [동] 구출하다
번역:
He died trying to rescue his cat.

의미: mess
예문:
[형] [명] 어질러 놓은 것, 엉망
번역:
What a mess!

의미: valid
예문:
[형] [형] 유효한, 타당한
번역:
You need a valid passport to cross the border.

의미: comprehensive
예문:
[형] [형] 종합적인
번역:
a comprehensive guide to making video

의미: cancel
예문:
[형] [동] 취소하다
번역:
The class has been canceled due to the virus.

의미: regret
예문:
[형] [동] 후회하다
번역:
I regret eating too much chicken at night.

의미: dismiss
예문:
[형] [동] (의견) 묵살하다, 떨쳐버리다
번역:
The boss just dismissed my opinion.

의미: resist
예문:
[형] [동] 참다, 막다, 저항하다
번역:
I just can't resist beer.

의미: correspond
예문:
[형] [동] 일치하다, 부합하다
번역:
수능 roughly corresponds to SAT in the US.

의미: stroke
예문:
[형] [명] (손) 한 번의 움직임, 치기
번역:
a backhand stroke

의미: dare
예문:
[형] [동] 감히 ~하다
번역:
He dared to fight against the government.

의미: barrier
예문:
[형] [명] 장벽, 장애물
번역:
Because of the language barrier, I couldn't move to China.

의미: vehicle
예문:
[형] [명] 차량
번역:
Two men hauled a woman into a vehicle.

의미: divorce
예문:
[형] [명] 이혼, 분리
번역:
Their marriage ended in divorce.

의미: ruin
예문:
[형] [동] (완전히) 망치다, 파괴하다
번역:
The cancer ruined his life.

의미: bury
예문:
[형] [동] (땅에)묻다
번역:
In the movie, the main character was buried alive.

의미: possess
예문:
[형] [동] (능력) 소유하다
번역:
Teachers must possess good computer skills.

의미: float
예문:
[형] [동] (물 위) 뜨다, 떠다니다
번역:
In fall, leaves are floating on water.

의미: verbal
예문:
[형] [형] 말의, 구두의
번역:
A presenter should have good verbal skills.

의미: evolution
예문:
[형] [명] 진화
번역:
Darwin's theory of evolution

의미: slave
예문:
[형] [명] 노예
번역:
a slave of money

의미: architecture
예문:
[형] [명] 건축학
번역:
겸모 studied architecture at university.

의미: coal
예문:
[형] [명] 석탄, 석탄조각
번역:
He put some coal on the fire.

의미: random
예문:
[형] [형] 무작위의
번역:
a group of housewives selected at random

의미: burst
예문:
[형] [동] 터지다
번역:
The balloon suddenly burst.

의미: privilege
예문:
[형] [명] 특권
번역:
Education shouldn't be a privilege only for the rich.

의미: mutual
예문:
[형] [형] 상호 간의, 공동의
번역:
Mutual respect is essential for a good relationship.

의미: motivate
예문:
[형] [동] 동기를 부여하다
번역:
It seems that most YouTubers are motivated by money. 

의미: laboratory
예문:
[형] [명] 실험실, 연구실
번역:
a research laboratory

의미: vertical
예문:
[형] [형] 수직의, 세로의
번역:
Alex Honnold climbed a 3,000-foot vertical cliff without ropes.

의미: mortgage
예문:
[형] [명] (담보) 대출(금)
번역:
We took out a 30-year mortgage to buy the apartment.

의미: passion
예문:
[형] [명] 열정
번역:
I have a passion for teaching English.

의미: fulfill
예문:
[형] [동] 충족하다, 완수하다
번역:
I want to fulfill my dream of writing an excellent English grammar book.

의미: dust
예문:
[형] [명] 먼지
번역:
The coronavirus has spread, and furthermore, the level of fine dust in the air has increased.

의미: dedicate
예문:
[형] [동] (시간, 노력을) 바치다
번역:
Dedicating more than 10 years of my life to learning English, I finally became a professional translator.

의미: province
예문:
[형] [명] 지역, 지방
번역:
Gyeonggi-do is a province of Korea.

의미: compromise
예문:
[형] [동] 타협하다
번역:
I never compromise my principles.

의미: accomplish
예문:
[형] [동] 완수하다
번역:
To accomplish great things, we must dream as well as act.

의미: glance
예문:
[형] [동] 흘꿋 보다
번역:
I try not to glance at my watch when I talk with someone.

의미: vibrant
예문:
[형] [형] 활기찬, 생기 넘치는
번역:
Hong Kong is a vibrant, fascinating city.

의미: embarrass
예문:
[형] [동] 당황스럽게 만들다
번역:
I don't want to embarrass you in front of other people.

의미: aggressive
예문:
[형] [형] 공격적인
번역:
Her voice became aggressive.

의미: chest
예문:
[형] [명] 가슴, 흉부
번역:
a hairy chest

의미: format
예문:
[형] [명] 형식
번역:
The format of Mr Trot resembles that of Miss Trot.

의미: embrace
예문:
[형] [동] 껴안다, 수용하다
번역:
I warmly embraced my daughter.

의미: praise
예문:
[형] [동] 칭찬하다
번역:
Parasite is a highly praised movie throughout the world.

의미: compensation
예문:
[형] [명] 보상금, 보상
번역:
claims for compensation

의미: deficit
예문:
[형] [명] 부족, 적자
번역:
a budget deficit of $2.5 million

의미: modify
예문:
[형] [동] (개선) 수정하다
번역:
The application is regularly modified to meet the users' needs.

의미: flash
예문:
[형] [명] 번쩍임
번역:
A flash of lightning lit up the night sky.

의미: literally
예문:
[형] [부] 문자 그대로
번역:
Big data literally means a vast quantity of data.

의미: equation
예문:
[형] [명] 방정식
번역:
For homework, solve the equations on page 34.

의미: assign
예문:
[형] [동] 맡기다, 부여하다
번역:
The judge was assigned to the case.

의미: remote
예문:
[형] [형] 멀리 떨어진
번역:
He has been living in a remote area for 5 years.

의미: therapy
예문:
[형] [명] 치료법
번역:
radiation therapy for cancer treatment

의미: throat
예문:
[형] [명] 목구멍
번역:
Most sore throats caused by a cold go away in a week.

의미: insight
예문:
[형] [명] 통찰력
번역:
Yuval Harari has a great insight.

의미: exceed
예문:
[형] [동] 초과하다
번역:
Netflix documentaries exceeded my expectations.

의미: expenditure
예문:
[형] [명] (특정 기간 중) 지출
번역:
Military expenditure has been growing year-on-year.

의미: pregnant
예문:
[형] [형] 임신한
번역:
If a pregnant woman smokes, the baby may fatally be injured.

의미: reliable
예문:
[형] [형] 믿을 만한, 확실한
번역:
He is a quiet and reliable man.

의미: fortune
예문:
[형] [명] 재산, 운
번역:
Warren Buffett has made a fortune on the stock market.

의미: ceremony
예문:
[형] [명] 의식, 식
번역:
an opening ceremony

의미: pile
예문:
[형] [명] 쌓아놓은 것, 무더기
번역:
There was a pile of pirate DVDs on his desk.

의미: automatically
예문:
[형] [부] 자동적으로
번역:
Excel will automatically calculate the sum.

의미: scholar
예문:
[형] [명] 학자
번역:
Newton was a brilliant scholar.

의미: stake
예문:
[형] [명] 말뚝, 지분
번역:
Mark Zuckerberg owns the biggest stake in Facebook.

의미: clause
예문:
[형] [명] 절, 조항
번역:
The penalty clause specifies that late delivery will be fined.

의미: penalty
예문:
[형] [명] 처벌, 벌금
번역:
The penalty clause specifies that late delivery will be fined.

의미: chamber
예문:
[형] [명] (사방이 막힌) 방, 실
번역:
The heart has four chambers.

의미: fancy
예문:
[형] [형] 화려한, 고급의
번역:
I took my wife to a fancy restaurant for our wedding anniversary.

의미: chat
예문:
[형] [동] 잡담하다
번역:
They were chatting at the bench.

의미: sake
예문:
[형] [명] 동기, 목적, 이유
번역:
For the sake of his health, he moved to a remote area.

의미: abortion
예문:
[형] [명] 낙태
번역:
She decided to have an abortion.

의미: tale
예문:
[형] [명] 이야기
번역:
a book of old folk tales

의미: maintenance
예문:
[형] [명] 유지, 정비
번역:
The website is regularly closed for routine maintenance.

의미: pot
예문:
[형] [명] 냄비, 단지
번역:
Most Korean foods need pots to cook.

의미: constraint
예문:
[형] [명] 제약, 제한
번역:
Most exams are done under strict time constraints.

의미: fold
예문:
[형] [동] 접다
번역:
Fold it in half.

의미: bin
예문:
[형] [명] 쓰레기통
번역:
I crumpled up the paper and pitched it into the bin.

의미: undergo
예문:
[형] [동] 겪다, 받다, 치르다
번역:
A new drug is undergoing clinical trials.

의미: scope
예문:
[형] [명] 범위, 여지
번역:
the scope of investigation

의미: pretend
예문:
[형] [동] ~인 척하다
번역:
The president is pretending that everything is fine.

의미: diversity
예문:
[형] [명] 다양성
번역:
Religious, cultural diversity must be respected by all.

의미: allege
예문:
[형] [동] 주장하다, 단언하다
번역:
It is alleged that she killed her ex-husband.

의미: pride
예문:
[형] [명] 자랑스러움, 자존심
번역:
Many Koreans have a sense of pride in their nationality.

의미: intense
예문:
[형] [형] 극심한, 치열한
번역:
There is intense competition for the job.

의미: inquiry
예문:
[형] [명] 질문, 조사 (=enquiry)
번역:
We have to prepare possible inquiries from potential customers.

의미: resign
예문:
[형] [동] 사직하다
번역:
Cho Guk resigned a month later after appointment to the post.

의미: craft
예문:
[형] [명] 공예, 기술
번역:
traditional crafts like straw-weaving

의미: strict
예문:
[형] [형] 엄격한, 엄밀한
번역:
The apartment has adopted a strict no-smoking policy.

의미: shell
예문:
[형] [명] (단단한) 껍데기
번역:
I used to collect shells on the beach.

의미: distinct
예문:
[형] [형] (확연히) 두드러지는, 구별되는
번역:
two distinct groups

의미: wise
예문:
[형] [형] 현명한
번역:
It is wise to leave home early not to be late.

의미: neglect
예문:
[형] [동] 방치하다, 소홀히하다
번역:
The young couple neglected their baby and let the baby die.

의미: compose
예문:
[형] [동] 구성하다, 작곡하다
번역:
Water is composed of hydrogen and oxygen.

의미: jail
예문:
[형] [명] 교도소
번역:
Cho will go to jail for a long time.

의미: shelter
예문:
[형] [명] 피난처
번역:
They are in need of food and shelter.

의미: carbon
예문:
[형] [명] 탄소
번역:
a carbon copy 

의미: trigger
예문:
[형] [동] (방아쇠를 당겨) 촉발시키다
번역:
Edward Snowden has triggered a massive public debate on privacy.

의미: destruction
예문:
[형] [명] 파괴, 파멸
번역:
the environmental destruction caused by plastic

의미: whisper
예문:
[형] [명] 속삭임
번역:
She said in a voice barely above a whisper.

의미: rear
예문:
[형] [형] 뒤쪽의
번역:
The rear doors of my car won't open from inside.

의미: species
예문:
[형] [명] (분류상의) 종
번역:
Pandas are endangered species.

의미: presumably
예문:
[형] [부] 추측하건대
번역:
For now, social distancing presumably is the only option to stop the pandemic.

의미: bless
예문:
[형] [동] 축복하다
번역:
May God bless you.

의미: amendment
예문:
[형] [명] 개정, 수정
번역:
How many amendments have been made to the US Constitution?

의미: jury
예문:
[형] [명] 배심원단
번역:
The jury found her not guilty.

의미: cooperation
예문:
[형] [명] 협력, 협동, 협조
번역:
This new electric vehicle has been made in cooperation with Tesla. 

의미: bunch
예문:
[형] [명] 다발, 묶음
번역:
I bought a bunch of bananas on my way home.

의미: greet
예문:
[형] [동] ~에게 인사하다, 맞이하다
번역:
She greeted me warmly.

의미: sanction
예문:
[형] [명] 제재
번역:
The US may impose sanctions on North Korea.

의미: trick
예문:
[형] [명] 속임수, 장난
번역:
I was getting tired of his silly tricks.

의미: paragraph
예문:
[형] [명] 단락, 문단
번역:
A paragraph consists of multiple sentences.

의미: stimulate
예문:
[형] [동] 자극하다
번역:
How can we stimulate the economy?

의미: narrative
예문:
[형] [명] (이야기 속 사건) 서술, 묘사
번역:
a compelling narrative of her journey to India

의미: barely
예문:
[형] [부] 간신히
번역:
She said in a voice barely above a whisper.

의미: invent
예문:
[형] [동] 발명하다
번역:
Who invented the internet?

의미: stair
예문:
[형] [명] 계단
번역:
Why do my knees hurt when climbing stairs?

의미: hesitate
예문:
[형] [동] 망설이다
번역:
She hesitated for a minute and said, 'no.'

의미: shine
예문:
[형] [동] 빛나다
번역:
Stars can't shine without darkness.

의미: stomach
예문:
[형] [명] 위, 배
번역:
I have a weak stomach.

의미: nowhere
예문:
[형] [부] 아무데도 ~않다
번역:
He had nowhere to live.

의미: pray
예문:
[형] [동] 기도하다
번역:
Let's pray for peace.

의미: servant
예문:
[형] [명] 하인
번역:
In east Calcutta, more than 80 per cent of the maid servants are illegal migrants from Bangladesh.

의미: immigrant
예문:
[형] [명] 이민자
번역:
integrate immigrants in society

의미: excess
예문:
[형] [명] 초과, 과다
번역:
an excess of enthusiasm

의미: liability
예문:
[형] [명] 법적 책임
번역:
legal liability for tax payment

의미: extract
예문:
[형] [동] 추출, 발췌하다
번역:
My daughter has to have the supernumerary tooth extracted.

의미: bias
예문:
[형] [명] 편견, 선입견
번역:
It is easy to see political bias in news media.

의미: envelope
예문:
[형] [명] 봉투
번역:
Only a few people use envelopes and stamps these days.

의미: biological
예문:
[형] [형] 생물학의
번역:
She finally found her biological mother.

의미: wherever
예문:
[형] [접] 어디서나
번역:
Some people enjoy themselves wherever they are.

의미: exhausted
예문:
[형] [형] 아주 피곤한, 기진맥진한
번역:
After running a marathon, I looked absolutely exhausted.

의미: veteran (vet)
예문:
[형] [명] 베테랑, 참전용사
번역:
이병헌 is a veteran actor.

의미: nerve
예문:
[형] [명] 신경, 초조함
번역:
I took a deep breath to calm my nerves.

의미: altogether
예문:
[형] [부] 모두 합쳐
번역:
How much do I owe you altogether?

의미: fiction
예문:
[형] [명] 소설, 허구
번역:
I don't like romantic fiction.

의미: cluster
예문:
[형] [명] 무리
번역:
A cluster of stars is called a galaxy.

의미: logic
예문:
[형] [명] 논리
번역:
Logic is the analysis of arguments.

의미: controversial
예문:
[형] [형] 논쟁의 여지가 있는
번역:
Politics and religion are controversial issues.

의미: raw
예문:
[형] [형] 날것의
번역:
raw material

의미: revise
예문:
[형] [동] 수정하다
번역:
All drafts need to be revised.

의미: hook
예문:
[형] [명] 갈고리
번역:
She always hung a towel on the hook on the wall.

의미: liquid
예문:
[형] [명] 액체
번역:
Water is a liquid.

의미: panic
예문:
[형] [명] 공포, 공황상태
번역:
She got into a panic when she lost her tuition fee.

의미: rice
예문:
[형] [명] 쌀
번역:
The main crops in Korea are rice, barley, and beans.

의미: slope
예문:
[형] [명] 경사면, 비탈
번역:
This SUV can climb a slope of 45 degrees.

의미: genuine
예문:
[형] [형] 진짜의, 진실된
번역:
This watch strap is genuine leather.

의미: vessel
예문:
[형] [명] 선박
번역:
Ultra large container vessels have a capacity of 15,000 or higher TEU.

의미: reckon
예문:
[형] [동] 생각하다, 짐작하다
번역:
Do you reckon she will come to the party?

의미: silly
예문:
[형] [형] 어리석은
번역:
I am getting tired of your silly tricks.

의미: harbor
예문:
[형] [명] 항구
번역:
The attack on Pearl Harbor was a surprise military strike.

의미: chase
예문:
[형] [동] 추격하다
번역:
The police chased the suspect.

의미: horrible
예문:
[형] [형] (오감 느낌이) 아주 나쁜 
번역:
Raw chicken tastes horrible.

의미: portrait
예문:
[형] [명] 초상화, 묘사
번역:
a portrait of King Sejong

의미: innocent
예문:
[형] [형] 죄가 없는
번역:
He was innocent of murder.

의미: substitute
예문:
[형] [동] ~로 대신하다, 대체하다
번역:
If you don't have oil, you can substitute butter for oil.

의미: flexible
예문:
[형] [형] 유연한, 구부러지는
번역:
What attracted me most to the job was the flexible working hours system.

의미: abstract
예문:
[형] [형] 추상적인
번역:
translate abstract ideas into words

의미: grain
예문:
[형] [명] 곡물, 한 톨
번역:
a grain of rice

의미: summarize
예문:
[형] [동] 요약하다
번역:
Summarize the story into one paragraph.

의미: leap
예문:
[형] [명] 도약, 점프
번역:
That's one small step for man, one giant leap for mankind.

의미: snap
예문:
[형] [동] 딱 하고 부러뜨리다
번역:
He snapped a pen in anger.

의미: leather
예문:
[형] [명] 가죽
번역:
This watch strap is genuine leather.

의미: swear
예문:
[형] [동] 맹세하다, 욕을 하다
번역:
Don't swear in front of the children.

의미: refugee
예문:
[형] [명] 난민
번역:
For refugee camps, Covid-19 is a death sentence.

의미: shore
예문:
[형] [명] 연안
번역:
"Shore" is a generic term for the place where land meets water.

의미: comprise
예문:
[형] [동] ~로 이루어지다
번역:
A paragraph comprises multiple sentences.

의미: stir
예문:
[형] [동] 휘젓다
번역:
She stirred her coffee with a pen.

의미: sigh
예문:
[형] [명] 한숨
번역:
She let out a sigh of disappointment.

의미: slice
예문:
[형] [명] (얇게 썬) 조각
번역:
a slice of bread

의미: wander
예문:
[형] [동] (정처없이) 천천히 걷다
번역:
I wandered around the department store for an hour.

의미: empire
예문:
[형] [명] 제국
번역:
An empire is a group of countries controlled by one ruler or government.

의미: ownership
예문:
[형] [명] 소유권
번역:
the ownership of the ship

의미: suspend
예문:
[형] [동] (띄워서) 멈추게 하다
번역:
The boy was suspended from school for two weeks.

의미: pale
예문:
[형] [형] 창백한, 색이 옅은
번역:
Even though I don't like pale blue jeans, I bought ones because they were really cheap.

의미: stain
예문:
[형] [명] 얼룩
번역:
There is a dark stain on the old and faded curtains.

의미: athlete
예문:
[형] [명] (육상 등) 운동선수
번역:
이봉주 is a professional athlete.

의미: tongue
예문:
[형] [명] 혀
번역:
Her sharp tongue will someday get her into trouble.

의미: unite
예문:
[형] [동] (다른 종류가) 연합하다
번역:
The world will be united someday.

의미: gently
예문:
[형] [부] 부드럽게, 살살
번역:
"It's time to go to bed," she gently said to her daughter.

의미: wipe
예문:
[형] [동] 쓸어내리며 닦다
번역:
Wipe the table with a wet tissue.

의미: weird
예문:
[형] [형] 이상한, 괴상한
번역:
UFOs are one of the weirdest things in the world.

의미: gaze
예문:
[형] [동] (오래, 멍) 응시하다
번역:
The dog gazed at me for a long time.

의미: fade
예문:
[형] [동] (색) 바래다, 사라지다
번역:
Youth fades, love droops, the leaves of friendship fall.

의미: cough
예문:
[형] [명] 기침, 기침 감기
번역:
COVID-19 symptoms include a sore throat and a cough.

의미: hypothesis
예문:
[형] [명] 가설
번역:
Further research will confirm the hypothesis.

의미: mayor
예문:
[형] [명] 시장
번역:
The mayor of Seoul is 박원순.

의미: registration
예문:
[형] [명] 등록, 신고
번역:
Advance registration is required for this workshop.

의미: fragment
예문:
[형] [명] 파편
번역:
Once glass is broken, the fragments are sharp and dangerous. 

의미: tender
예문:
[형] [형] 부드러운, 연약한
번역:
I want to know how to make tough meat tender.

의미: density
예문:
[형] [명] 밀도
번역:
Seoul has high population density.

의미: cheek
예문:
[형] [명] 볼, 뺨
번역:
When I kissed her on the cheek, she grinned at me.

의미: grin
예문:
[형] [동] 활짝 웃다
번역:
When I kissed her on the cheek, she grinned at me.

의미: hunger
예문:
[형] [명] 배고픔, 열망
번역:
I have a hunger for success.

의미: ashamed
예문:
[형] [형] (잘못해서) 부끄럽고 창피한
번역:
You should be ashamed of yourself!


"""


def process_text(text):
    data = []
    entries = re.split(r'\n\s*\n', text.strip())

    for entry in entries:
        meaning_match = re.search(r'의미:\s(.+)', entry)
        sentence_match = re.search(r'예문:\s(.+)', entry)
        translation_match = re.search(r'번역:\s(.+)', entry)

        if meaning_match and sentence_match and translation_match:
            meaning = meaning_match.group(1)
            sentence = sentence_match.group(1)
            translation = translation_match.group(1)

            # Remove [형] appearing once
            sentence = re.sub(r'\[(.*?)\]', '', sentence).strip()

            data.append({
                "의미": meaning,
                "예문": sentence,
                "번역": translation
            })

    return data

processed_data = process_text(text)
output_file = "output.json"

with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(processed_data, json_file, indent=4, ensure_ascii=False)

print(f"Data saved to {output_file}")