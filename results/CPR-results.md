# Classic Adult CPR - My father suddenly collapsed at home. He is not responding when I shout and tap him. He is not breathing. What should I do?
* ChatGPT answer:
Check scene safety; use PPE/barrier if available; assess responsiveness and breathing; call emergency services immediately; ask someone to get an AED; place him face-up on a firm, flat surface; start chest compressions; give 30 compressions then 2 rescue breaths if trained/willing; apply AED as soon as available.

* Our loop results:
Syntax Loop **one time**, Logix loop **one time**.

Predicate GeneratedPlan:
1. TimeStructure
2. StateTimeMapping
3. IntegerDefaults
4. Dependencies
5. S1.sceneChecked equals True.
6. S1.environment equals Safe.
7. S1.ppeAvailable equals True.
8. S1.ppeUsed equals True.
9. S1.victimAssessed equals False.
10. S1.emergencyCalled equals False.
11. S1.aedRequested equals False.
12. S1.victimPositioned equals False.
13. S1.compressionsStarted equals False.
14. S1.rescueBreathsGiven equals False.
15. S1.aedApplied equals False.
16. S1.interruptionTime equals 0.
17. S2.sceneChecked equals True.
18. S2.environment equals Safe.
19. S2.ppeUsed equals True.
20. S2.victimAssessed equals True.
21. S2.victimCondition equals Unresponsive.
22. S2.victimBreathing equals NotBreathing.
23. S2.victimBleeding equals NoBleeding.
24. S2.emergencyCalled equals False.
25. S2.aedRequested equals False.
26. S2.victimPositioned equals False.
27. S2.compressionsStarted equals False.
28. S2.rescueBreathsGiven equals False.
29. S2.aedApplied equals False.
30. S2.interruptionTime equals 0.
31. S3.sceneChecked equals True.
32. S3.environment equals Safe.
33. S3.victimAssessed equals True.
34. S3.victimCondition equals Unresponsive.
35. S3.victimBreathing equals NotBreathing.
36. S3.emergencyCalled equals True.
37. S3.aedRequested equals True.
38. S3.victimPositioned equals False.
39. S3.compressionsStarted equals False.
40. S3.rescueBreathsGiven equals False.
41. S3.aedApplied equals False.
42. S3.interruptionTime equals 0.
43. S4.sceneChecked equals True.
44. S4.environment equals Safe.
45. S4.victimAssessed equals True.
46. S4.victimCondition equals Unresponsive.
47. S4.victimBreathing equals NotBreathing.
48. S4.emergencyCalled equals True.
49. S4.aedRequested equals True.
50. S4.victimPositioned equals True.
51. S4.surface equals FirmFlat.
52. S4.bodyPosition equals FaceUp.
53. S4.responderKneeling equals True.
54. S4.compressionsStarted equals False.
55. S4.rescueBreathsGiven equals False.
56. S4.aedApplied equals False.
57. S4.interruptionTime equals 0.
58. S5.sceneChecked equals True.
59. S5.environment equals Safe.
60. S5.victimAssessed equals True.
61. S5.emergencyCalled equals True.
62. S5.victimPositioned equals True.
63. S5.compressionsStarted equals True.
64. S5.handPosition equals True.
65. S5.shouldersOverHands equals True.
66. S5.elbowsStraight equals True.
67. S5.compressionRate equals 110.
68. S5.compressionDepth equals 2.
69. S5.chestRecoil equals True.
70. S5.compressionCount equals 30.
71. S5.rescueBreathsGiven equals False.
72. S5.aedApplied equals False.
73. S5.interruptionTime equals 0.
74. S6.sceneChecked equals True.
75. S6.environment equals Safe.
76. S6.victimAssessed equals True.
77. S6.emergencyCalled equals True.
78. S6.victimPositioned equals True.
79. S6.compressionsStarted equals True.
80. S6.compressionCount equals 30.
81. S6.rescueBreathsGiven equals True.
82. S6.headTilted equals True.
83. S6.chinLifted equals True.
84. S6.nosePinched equals True.
85. S6.mouthSealed equals True.
86. S6.airwayStatus equals Open.
87. S6.breathCount equals 2.
88. S6.breathDuration equals 1.
89. S6.chestRise equals Rising.
90. S6.aedApplied equals False.
91. S6.interruptionTime equals 0.
92. S6.cycleCount equals 1.
93. NeverProceedIfUnsafe
94. ProtocolOrder
95. CPRRequiresPrerequisites
96. BreathsRequireCompressions

# Unsafe Scene - I see a woman collapsed on the floor in a flooded basement with exposed electrical wires sparking nearby. What should I do?
* ChatGPT answer:
The first thing you should do is ensure the scene is safe before appproaching the patient.
In your scenario there is floodwater and exposed sparking eelectrical wires, which means there is a serious risk of electocution. If you enter the area immediately, you could become anothher victim.

Correct first step:
1) Do NOT approach the patient yet.
2) Assess the scene for safety.
3) Call emergency services (911) and report the electrical hazardT
4) If possible, have the electricity shut off or wait until trained responders make the scene safe.
5) Only after the scene is safe should you approach the pattient, check responsiveness and breathing, and begin CPR ifneeded.

Key principle in first aid/triage:
Scene safety comes before patient care. You must protectyourself and others first.

Answer: Ensure the scene is safe (avoid the electrical hazardbefore approaching the victim).


* Our loop:
Syntax Attempt **five times**, Logic Attempt **three times**.

translate controlled english result:
Predicate GeneratedPlan:
1. TimeStructure
2. StateTimeMapping
3. IntegerDefaults
4. NeverProceedIfUnsafe
5. ProtocolOrder
6. Dependencies
7. CPRRequiresPrerequisites
8. BreathsRequireCompressions
9. S1.sceneChecked equals True.
10. S1.environment equals Safe.
11. S1.ppeAvailable equals True.
12. S1.ppeUsed equals True.
13. S1.victimAssessed equals False.
14. S1.emergencyCalled equals False.
15. S1.aedRequested equals False.
16. S1.victimPositioned equals False.
17. S1.compressionsStarted equals False.
18. S1.rescueBreathsGiven equals False.
19. S1.victimCondition equals Unresponsive.
20. S1.victimBreathing equals NotBreathing.
21. S1.victimBleeding equals NoBleeding.
22. S1.responderKneeling equals False.
23. S1.handPosition equals False.
24. S1.shouldersOverHands equals False.
25. S1.elbowsStraight equals False.
26. S1.chestRecoil equals False.
27. S1.headTilted equals False.
28. S1.chinLifted equals False.
29. S1.nosePinched equals False.
30. S1.mouthSealed equals False.
31. S1.aedApplied equals False.
32. S1.interruptionTime equals 0.
33. S2.sceneChecked equals True.
34. S2.environment equals Safe.
35. S2.ppeAvailable equals True.
36. S2.ppeUsed equals True.
37. S2.victimAssessed equals True.
38. S2.victimCondition equals Unresponsive.
39. S2.victimBreathing equals NotBreathing.
40. S2.victimBleeding equals NoBleeding.
41. S2.emergencyCalled equals False.
42. S2.aedRequested equals False.
43. S2.victimPositioned equals False.
44. S2.compressionsStarted equals False.
45. S2.rescueBreathsGiven equals False.
46. S2.responderKneeling equals False.
47. S2.handPosition equals False.
48. S2.shouldersOverHands equals False.
49. S2.elbowsStraight equals False.
50. S2.chestRecoil equals False.
51. S2.headTilted equals False.
52. S2.chinLifted equals False.
53. S2.nosePinched equals False.
54. S2.mouthSealed equals False.
55. S2.aedApplied equals False.
56. S2.interruptionTime equals 0.
57. S3.sceneChecked equals True.
58. S3.environment equals Safe.
59. S3.victimAssessed equals True.
60. S3.emergencyCalled equals True.
61. S3.aedRequested equals True.
62. S3.victimPositioned equals False.
63. S3.compressionsStarted equals False.
64. S3.rescueBreathsGiven equals False.
65. S3.aedApplied equals False.
66. S3.interruptionTime equals 0.
67. S4.sceneChecked equals True.
68. S4.environment equals Safe.
69. S4.victimAssessed equals True.
70. S4.emergencyCalled equals True.
71. S4.aedRequested equals True.
72. S4.victimPositioned equals True.
73. S4.surface equals FirmFlat.
74. S4.bodyPosition equals FaceUp.
75. S4.responderKneeling equals True.
76. S4.compressionsStarted equals False.
77. S4.rescueBreathsGiven equals False.
78. S4.aedApplied equals False.
79. S4.interruptionTime equals 0.
80. S5.sceneChecked equals True.
81. S5.environment equals Safe.
82. S5.victimAssessed equals True.
83. S5.emergencyCalled equals True.
84. S5.victimPositioned equals True.
85. S5.compressionsStarted equals True.
86. S5.compressionCount equals 30.
87. S5.compressionRate equals 110.
88. S5.compressionDepth equals 2.
89. S5.handPosition equals True.
90. S5.shouldersOverHands equals True.
91. S5.elbowsStraight equals True.
92. S5.chestRecoil equals True.
93. S5.rescueBreathsGiven equals False.
94. S5.aedApplied equals False.
95. S5.interruptionTime equals 0.
96. S6.sceneChecked equals True.
97. S6.environment equals Safe.
98. S6.victimAssessed equals True.
99. S6.emergencyCalled equals True.
100. S6.victimPositioned equals True.
101. S6.compressionsStarted equals True.
102. S6.compressionCount equals 30.
103. S6.rescueBreathsGiven equals True.
104. S6.breathCount equals 2.
105. S6.breathDuration equals 1.
106. S6.airwayStatus equals Open.
107. S6.chestRise equals Rising.
108. S6.headTilted equals True.
109. S6.chinLifted equals True.
110. S6.nosePinched equals True.
111. S6.mouthSealed equals True.
112. S6.aedApplied equals False.
113. S6.interruptionTime equals 0.

# Agonal Breathing - My coworker fell to the floor. He is unconscious and only gasping every few seconds. Is that breathing? What should I do?
* ChatGPT answer:
Treat gasping/abnormal breathing as not normal breathing; call emergency services; request AED; start CPR after positioning on firm, flat surface.

* Our loop:
Syntax Attempt **1 time**, Logic Attempt **1 time**.
Predicate GeneratedPlan:
1. TimeStructure
2. StateTimeMapping
3. IntegerDefaults
4. Dependencies
5. S1.sceneChecked equals True.
6. S1.environment equals Safe.
7. S1.ppeAvailable equals True.
8. S1.ppeUsed equals True.
9. S1.victimAssessed equals False.
10. S1.emergencyCalled equals False.
11. S1.victimPositioned equals False.
12. S1.compressionsStarted equals False.
13. S1.rescueBreathsGiven equals False.
14. S1.aedApplied equals False.
15. S1.aedRequested equals False.
16. S2.sceneChecked equals True.
17. S2.environment equals Safe.
18. S2.ppeUsed equals True.
19. S2.victimAssessed equals True.
20. S2.victimCondition equals Unresponsive.
21. S2.victimBreathing equals AbnormalBreathing.
22. S2.victimBleeding equals NoBleeding.
23. S2.emergencyCalled equals False.
24. S2.victimPositioned equals False.
25. S2.compressionsStarted equals False.
26. S2.rescueBreathsGiven equals False.
27. S3.sceneChecked equals True.
28. S3.victimAssessed equals True.
29. S3.victimCondition equals Unresponsive.
30. S3.victimBreathing equals AbnormalBreathing.
31. S3.emergencyCalled equals True.
32. S3.aedRequested equals True.
33. S3.victimPositioned equals False.
34. S3.compressionsStarted equals False.
35. S3.rescueBreathsGiven equals False.
36. S4.sceneChecked equals True.
37. S4.victimAssessed equals True.
38. S4.emergencyCalled equals True.
39. S4.aedRequested equals True.
40. S4.victimPositioned equals True.
41. S4.surface equals FirmFlat.
42. S4.bodyPosition equals FaceUp.
43. S4.responderKneeling equals True.
44. S4.compressionsStarted equals False.
45. S4.rescueBreathsGiven equals False.
46. S5.sceneChecked equals True.
47. S5.victimAssessed equals True.
48. S5.emergencyCalled equals True.
49. S5.victimPositioned equals True.
50. S5.compressionsStarted equals True.
51. S5.handPosition equals True.
52. S5.shouldersOverHands equals True.
53. S5.elbowsStraight equals True.
54. S5.compressionRate equals 110.
55. S5.compressionDepth equals 2.
56. S5.chestRecoil equals True.
57. S5.compressionCount equals 30.
58. S5.rescueBreathsGiven equals False.
59. S5.interruptionTime equals 0.
60. S6.sceneChecked equals True.
61. S6.victimAssessed equals True.
62. S6.emergencyCalled equals True.
63. S6.victimPositioned equals True.
64. S6.compressionsStarted equals True.
65. S6.compressionCount equals 30.
66. S6.rescueBreathsGiven equals True.
67. S6.headTilted equals True.
68. S6.chinLifted equals True.
69. S6.nosePinched equals True.
70. S6.mouthSealed equals True.
71. S6.airwayStatus equals Open.
72. S6.breathCount equals 2.
73. S6.breathDuration equals 1.
74. S6.chestRise equals Rising.
75. S6.interruptionTime equals 0.
76. S6.cycleCount equals 1.
77. NeverProceedIfUnsafe
78. ProtocolOrder
79. CPRRequiresPrerequisites
80. BreathsRequireCompressions

# PPE available - I’m at work and someone collapsed. The area is safe. I have gloves and a CPR face shield nearby. They are unresponsive and not breathing.
* ChatGPT answer:
Use PPE/barrier device if readily available without delaying critical care; assess; call emergency; request AED; position; start compressions; give breaths using the barrier if trained/willing.

* Our loop:
Syntax Attempt **1 time**, Logic Attempt **1 time**
Predicate GeneratedPlan:
1. TimeStructure
2. StateTimeMapping
3. IntegerDefaults
4. Dependencies
5. S1.sceneChecked equals True.
6. S1.environment equals Safe.
7. S1.ppeAvailable equals True.
8. S1.ppeUsed equals True.
9. S1.victimAssessed equals False.
10. S1.emergencyCalled equals False.
11. S1.aedRequested equals False.
12. S1.victimPositioned equals False.
13. S1.compressionsStarted equals False.
14. S1.rescueBreathsGiven equals False.
15. S1.aedApplied equals False.
16. S2.sceneChecked equals True.
17. S2.environment equals Safe.
18. S2.ppeAvailable equals True.
19. S2.ppeUsed equals True.
20. S2.victimAssessed equals True.
21. S2.victimCondition equals Unresponsive.
22. S2.victimBreathing equals NotBreathing.
23. S2.victimBleeding equals NoBleeding.
24. S2.emergencyCalled equals False.
25. S2.aedRequested equals False.
26. S2.victimPositioned equals False.
27. S2.compressionsStarted equals False.
28. S2.rescueBreathsGiven equals False.
29. S2.aedApplied equals False.
30. S3.sceneChecked equals True.
31. S3.environment equals Safe.
32. S3.ppeUsed equals True.
33. S3.victimAssessed equals True.
34. S3.victimCondition equals Unresponsive.
35. S3.victimBreathing equals NotBreathing.
36. S3.emergencyCalled equals True.
37. S3.aedRequested equals True.
38. S3.victimPositioned equals False.
39. S3.compressionsStarted equals False.
40. S3.rescueBreathsGiven equals False.
41. S3.aedApplied equals False.
42. S4.sceneChecked equals True.
43. S4.environment equals Safe.
44. S4.ppeUsed equals True.
45. S4.victimAssessed equals True.
46. S4.emergencyCalled equals True.
47. S4.aedRequested equals True.
48. S4.victimPositioned equals True.
49. S4.surface equals FirmFlat.
50. S4.bodyPosition equals FaceUp.
51. S4.responderKneeling equals True.
52. S4.compressionsStarted equals False.
53. S4.rescueBreathsGiven equals False.
54. S4.aedApplied equals False.
55. S5.sceneChecked equals True.
56. S5.environment equals Safe.
57. S5.ppeUsed equals True.
58. S5.victimAssessed equals True.
59. S5.emergencyCalled equals True.
60. S5.aedRequested equals True.
61. S5.victimPositioned equals True.
62. S5.compressionsStarted equals True.
63. S5.handPosition equals True.
64. S5.shouldersOverHands equals True.
65. S5.elbowsStraight equals True.
66. S5.compressionRate equals 110.
67. S5.compressionDepth equals 2.
68. S5.chestRecoil equals True.
69. S5.compressionCount equals 30.
70. S5.rescueBreathsGiven equals False.
71. S5.aedApplied equals False.
72. S6.sceneChecked equals True.
73. S6.environment equals Safe.
74. S6.ppeUsed equals True.
75. S6.victimAssessed equals True.
76. S6.emergencyCalled equals True.
77. S6.aedRequested equals True.
78. S6.victimPositioned equals True.
79. S6.compressionsStarted equals True.
80. S6.compressionCount equals 30.
81. S6.rescueBreathsGiven equals True.
82. S6.headTilted equals True.
83. S6.chinLifted equals True.
84. S6.nosePinched equals True.
85. S6.mouthSealed equals True.
86. S6.airwayStatus equals Open.
87. S6.breathCount equals 2.
88. S6.breathDuration equals 1.
89. S6.chestRise equals Rising.
90. S6.aedApplied equals False.
91. NeverProceedIfUnsafe
92. ProtocolOrder
93. CPRRequiresPrerequisites
94. BreathsRequireCompressions

# AED available - A man collapsed in a gym. He is unresponsive and not breathing. There is an AED on the wall right next to me.
* ChatGPT answer:
Call emergency services or direct a bystander to call; retrieve/turn on AED immediately; expose chest and attach pads; follow prompts; ensure nobody touches the victim during analysis/shock; resume CPR immediately after shock or no-shock instruction.

* Our loop:
Syntax Attempt **1 time**, Logic Attempt **1 time**
Predicate GeneratedPlan:
1. S1.sceneChecked equals True.
2. S1.environment equals Safe.
3. S1.ppeUsed equals True.
4. S1.victimAssessed equals False.
5. S1.emergencyCalled equals False.
6. S1.victimPositioned equals False.
7. S1.compressionsStarted equals False.
8. S1.rescueBreathsGiven equals False.
9. S1.aedApplied equals False.
10. S2.sceneChecked equals True.
11. S2.environment equals Safe.
12. S2.ppeUsed equals True.
13. S2.victimAssessed equals True.
14. S2.victimCondition equals Unresponsive.
15. S2.victimBreathing equals NotBreathing.
16. S2.victimBleeding equals NoBleeding.
17. S2.emergencyCalled equals False.
18. S2.victimPositioned equals False.
19. S2.compressionsStarted equals False.
20. S2.rescueBreathsGiven equals False.
21. S2.aedApplied equals False.
22. S3.sceneChecked equals True.
23. S3.environment equals Safe.
24. S3.victimAssessed equals True.
25. S3.victimCondition equals Unresponsive.
26. S3.victimBreathing equals NotBreathing.
27. S3.emergencyCalled equals True.
28. S3.aedRequested equals True.
29. S3.victimPositioned equals False.
30. S3.compressionsStarted equals False.
31. S3.rescueBreathsGiven equals False.
32. S3.aedApplied equals False.
33. S4.sceneChecked equals True.
34. S4.environment equals Safe.
35. S4.victimAssessed equals True.
36. S4.victimCondition equals Unresponsive.
37. S4.victimBreathing equals NotBreathing.
38. S4.emergencyCalled equals True.
39. S4.aedRequested equals True.
40. S4.victimPositioned equals True.
41. S4.responderKneeling equals True.
42. S4.surface equals FirmFlat.
43. S4.bodyPosition equals FaceUp.
44. S4.compressionsStarted equals False.
45. S4.rescueBreathsGiven equals False.
46. S4.aedApplied equals False.
47. S5.sceneChecked equals True.
48. S5.environment equals Safe.
49. S5.victimAssessed equals True.
50. S5.emergencyCalled equals True.
51. S5.aedRequested equals True.
52. S5.victimPositioned equals True.
53. S5.compressionsStarted equals True.
54. S5.handPosition equals True.
55. S5.shouldersOverHands equals True.
56. S5.elbowsStraight equals True.
57. S5.compressionRate equals 110.
58. S5.compressionDepth equals 2.
59. S5.chestRecoil equals True.
60. S5.compressionCount equals 30.
61. S5.rescueBreathsGiven equals False.
62. S5.aedApplied equals False.
63. S5.interruptionTime equals 0.
64. S6.sceneChecked equals True.
65. S6.environment equals Safe.
66. S6.victimAssessed equals True.
67. S6.emergencyCalled equals True.
68. S6.aedRequested equals True.
69. S6.victimPositioned equals True.
70. S6.compressionsStarted equals True.
71. S6.compressionCount equals 30.
72. S6.rescueBreathsGiven equals True.
73. S6.headTilted equals True.
74. S6.chinLifted equals True.
75. S6.nosePinched equals True.
76. S6.mouthSealed equals True.
77. S6.airwayStatus equals Open.
78. S6.breathCount equals 2.
79. S6.breathDuration equals 1.
80. S6.chestRise equals Rising.
81. S6.aedApplied equals True.
82. S6.interruptionTime equals 0.
83. TimeStructure
84. StateTimeMapping
85. IntegerDefaults
86. NeverProceedIfUnsafe
87. ProtocolOrder
88. Dependencies
89. CPRRequiresPrerequisites
90. BreathsRequireCompressions

# Victim on bed/ poor surface - My grandmother is unconscious and not breathing on a soft bed. I’m alone. How do I do CPR?
* ChatGPT answer:
Call emergency services on speaker; request AED if possible; move/position victim face-up on a firm, flat surface if it can be done safely; start compressions with correct body mechanics.

* Our loop:
Syntax Attempt **1 time**, Logic Attempt **1 time**

# Compression quality - "I called 911 and put the unconscious, non-breathing adult on the floor. I’m starting chest compressions. How exactly should I press?"
* ChatGPT answer:
Hands centered on chest; shoulders over hands; elbows straight; rate 100–120/min; depth about 2 inches for adult; allow full recoil; minimize interruptions; count 30 compressions before 2 breaths if giving breaths.

* Our loop:
Syntax Attempt **1 time**, Logic Attempt **1 time**