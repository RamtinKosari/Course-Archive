# 01 - Intro to AI, Rational Agents
<img src="https://img.shields.io/badge/status-on%20going-cyan?&labelColor=344250&color=4CAAAF"/> <img src="https://img.shields.io/badge/start date-18%20july%202025-cyan?&labelColor=344250&color=7799AF"/> <img src="https://img.shields.io/badge/project-Under%20Develop-cyan?&labelColor=344250&color=7799CF"/> <img src="https://img.shields.io/github/contributors/ramtinkosari/Course-Archive?color=77778F&labelColor=344250"/>

UC Berkeley CS 188 Spring 2024 Course, Lesson 1
Thanks to ```Cameron Allen```, ```Michael Cohen``` and other course staffs

## What is Artificial Intelligence ?
##### AI is having real-world impacts
Text assistants, Image generation and ..., who can live without it ? 
it has been impacted on economy, politics, law, labor (taking our jobs), sciences and educations
- The global AI market size till 2022 was USD 454.12 billion, now it is [USD 638.23 billion](https://www.precedenceresearch.com/artificial-intelligence-market). government is trying to controll this market which is why heads of AI companies meeting with the heads of The United States government even with heads of other countires. These companies have now a lot of political power.
- AI also impacts law, because we're trying to wrangle with what's the legality of these systems like ```when they are trained on these big datasets and these datasets just come from the internet and some of the internet is copyrighted```, [what happens ?](https://news.bloomberglaw.com/ip-law/ai-generated-art-lacks-copyright-protection-d-c-court-rules). we're still trying to figure out how to handle these kinds of things legally.
- There's the labor angle. there's always the jobs angle, so the AIs are going to come and take all our jobs. and so there are some articles that say [***watch out for the AI, it's coming for your jobs***](https://www.economist.com/finance-and-economics/2021/01/16/new-research-shows-the-robots-are-coming-for-jobs-but-stealthily) and there's are other articles that are like [***actually, we should be optimistic, they're not coming for all the jobs, maybe they're creating jobs too***](https://www.nytimes.com/2023/05/20/business/dealbook/the-optimists-guide-to-artificial-intelligence-and-work.html) and then there's articles that are like [***yeah, what jobs are they creating, globally? are these the jobs that we want them to create?***](https://www.marketplace.org/episode/2023/03/21/the-human-labor-behind-ai-chatbots-and-other-smart-tools)
- Meanwhile it's having an impact on science, like [AlphaFold](https://www.nature.com/articles/d41586-022-02999-9) discovery, which was a breakthrough in the protein-folding problem a couple of years ago and DeepMind won this big prize for basically you take a sequence of amino acids and then you figure out how it turns into a 3D protein object. this has been a long-standing problem in drug discovery and the life sciences, more broadly. even not just in discovery but in control like another DeepMind project which is [controlling nuclear fusion using AI](https://www.wired.com/story/deepmind-ai-nuclear-fusion/).
- And in education, then there's all these questions about why [ChatGPT should be banned in schools](https://www.forbes.com/sites/ariannajohnson/2023/01/18/chatgpt-in-schools-heres-where-its-banned-and-how-it-could-potentially-help-students/).

##### Ok, but what actually is AI?
What should we build ?
* Make machines that ***think like people*** ?
  * Classical cognitive science, neuroscience-style approach
  * But the thing is, we don't always know how people think, we just know that we can observe what they're doing so maybe it's better if we ...
* Make machines that ***act like people*** ?
  * Very old definition back to Alan Turing. the Turing Test is a classic example of this : ***If a machine acts like a person and it's indistinguishable in terms of behavior from a person, maybe that's the mark of intelligence***, any problem with this ?
    1. if you have a machine that's trying to pretend to be a human or trying to act like a person, to a certain extent, it's going to have to do things that human do. that might not be desirable liek getting wrong asnwers to math questions and having a favorite color.
    2. we have already about 8 billion humans, so do we really need to design systems that act like us and be what we are ? we have enough of those. 
* Make machines that ***think rationally*** ?
  * This is the classic aristotle version of intelligence, it's like ***have the right thought process, it should lead you to the right conclusions***. Its nice idea but it doesn't quite get you all the way there, because you can think forever and if you don't actually do something with all that thinking, it doesn't really mean that you've demonstrated being intelligent.
* Make machines that ***act rationally*** ?
  * This is the key to all of it. this course will take the stance that is the way to go about it.

##### Rational Decisions
we'll use the term ```Rational``` in a very specific, technical way :
* ***Rational :*** maximally achieving predefined goals
* Goals are expressed in terms of the ***utility*** of outcomes
* World is uncertain, so we'll use ***expected*** utility
* Being rational means acting to maximize your expected utility

***It doesn't really matter how you're thinking, as long as your actions correspond to whatever brings about the biggest expected utility.***
A better name for this course should be ```Computational Rationality```.

##### Perspectives on Intelligence
sssss
