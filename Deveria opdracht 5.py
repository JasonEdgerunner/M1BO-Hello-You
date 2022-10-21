from multiprocessing.resource_sharer import stop
from os import kill
from tkinter import Variable
from time import sleep
while True:
    print("Welcome to The Deveria Descent.")
    sleep(2)
    print("This is a story about a demonic creature, named Tichettio.")
    sleep(2)
    print("Tichettio is a Deveria, a demon known for their volatile nature and ability to blast explosions from their palms.")
    sleep(2)
    print("But he is different, capable of travelling outside of this demonic wasteland. What will Tichettio do with this knowledge? His actions are decided by none other than you. Good luck.")
    sleep(2)

    print("Fire, ashes and the body parts of your friends and family, all soaring through the air.")
    sleep(1.5)
    print("You're familiar with this place, it's where you were born. But today, you were invited to the current leader of the Deveria.")
    sleep(1.5)
    print("Will you:")
    sleep(1.5)
    print("A. Go to the leader, I want to see what they want.")
    sleep(0.8)
    print("B. No way I'm going there! Fuck the corporate hierarchy of this wretched place!")
    sleep(0.8)
    print("C. I shall go, but I'm keeping my guard up. I don't know who the leader is.")
    path1 = input()
    if path1 == "A":
        print("You decided to go the leader, the strangers you have come to grow and hate are all yelling in fear. You're not one of great reputation.")
        sleep(1.4)
        print("As you walk through the wastelands, covered by soot and the charred bodies of the ones you once knew, you come across a tall castle. It reads 'The King'")
        sleep(1.4)
        print("Your heart pounds faster as you keep inching closer, the inches thick steel doors growing before you with each step. The feeling of dread, like this could be your end now, dawns on your body.")
        sleep(1.4)
        print("Slowly, the doors open. You expected a self defense mechanism, something to immediately blow you to pieces, but you were met by an incredibly tall, buff individual. 'Welcome. We've been expecting you, Tichettio. Follow me please.' The tall man turned away and walked in front of you, hands clasped neatly behind his back. Seems like this is the bouncer.")
        sleep(3)
    if path1 == "B":
        print("'Fuck them! You're your own Deveria right?! No way you would be controlled by that ugly sack of-' Before you could finish your thoughts, you were blinded by an explosion right next to your face. Your head rolls off. Guess it's not safe to stay here.")
        sleep(1)
        print("So that's it then. You chose anarchy in a world dominated by the anarchists. You rebelled against rebellion. I commend your spirit, but this is the end. Would you like to play again? Please type Y or N.") 
        again = input()
        if again == "Y":
            print("Good luck to you then.")
            sleep(1.25)
        if again == "N":
            break
    if path1 == "C":
        print("You're on your way, but you're wary of who you're looking at. After all, you're not much liked. But this overly protective behavior of yourself made you too observant, not only adding 'douchebag' to the list of crimes, but murderer as well as you blast the head off of your best friend's body. A shame really, he was the only one you felt you could trust.")
        sleep(1.5)
        print("As you walk through the wastelands, covered by soot and the charred bodies of the ones you once knew, you come across a tall castle. It reads 'The King'")
        sleep(1.4)
        print("Your heart pounds faster as you keep inching closer, the inches thick steel doors growing before you with each step. The feeling of dread, like this could be your end now, dawns on your body.")
        sleep(1.4)
        print("Slowly, the doors open. You expected a self defense mechanism, something to immediately blow you to pieces, but you were met by an incredibly tall, buff individual. 'Welcome. We've been expecting you, Tichettio. Follow me please.' The tall man turned away and walked in front of you, hands clasped neatly behind his back. Seems like this is the bouncer.")
        sleep(3)
    print("You follow the tall man into the castle halls, the doors slamming shut violently behind you. You turn around and see a fresh arm, snapped right off the body from a Deveria who attempted to intrude the castle. It crackled softly before laying there, limp and completely still. It seemed like this king knew what he was doing, an excellent defense system that didn't falter to protect the royalties of this wretched place.")
    sleep(1.5)
    print("The castle seemed barren, only fashioned with the essential walls, guard railings for the stairs and the occasional torch. Illegal import from the Quissers, water based torches that not even the strongest Deveria could hope to douse.")
    sleep(1.5)
    print("As you keep going through the castle hall, a continuously louder sound of punk music starts to ring in your ears. The closer you got, the more it sounded like an underground punk concert rather than a house of royals.")
    sleep(1.5)
    print("And there he sat, the king of the Deveria, Johnny Chars. Not much unlike the usual rocker, fashioned with a leather jacket covered in spikes and symbols of anarchists. You didn't realize it, until you heard his voice. You realized this was your other friend, the only person you could absolutely trust with everything, the one who would throw his life away just to protect yours.")
    sleep(1.5)
    print("Heeey Ticking Timebomb! Been way too long man, you finally found out what you can do with your powers huh? Don't answer that, you wouldn't be here if you didn't!' He followed his chatter up with a hearty laugh, one reminding you of the childhood you had, warming your soul as if it was a long overdue hug. Speaking of which...")
    sleep(1.5)
    print("Johnny got up from his throne and ran down the stairs, immediately jumping in your arms, giving you a long and warm hug, coming in with a gentle kiss on the lips. You react to this with a...")
    sleep(1.5)
    print("A. You wrap your arms around Johnny's waist and pull him in for the hug but you keep your lips away from his, letting out a gentle laugh. 'So you became king huh? Man, here I thought I was successful just being alive!'")
    sleep(0.8)
    print("B. You shove Johnny away out of the hug, giving him a punch in the gut for trying to kiss you! Fucker's a king now and left you to die? Piss off. 'Oh suck a fat one Johnny, you left me out in that wasteland hoping I'd fall dead. What do you want from me.'")
    sleep(0.8)
    print("C. Your arms wrap around Johnny's neck, your lips softly being placed on his as you keep yourself close to your childhood friend. Seems like the feelings of just your past go beyond a friendly buddy-buddy relationship! 'It's been way too long Johnny, I missed you. But I got the feeling I will be missing you again soon, otherwise you didn't call me on an urgent mail. Unless you want to announce to the people there are two kings now.'")
    path2 = input()
    if path2 == "A":
        print("Johnny understood the hint, giving you a last squeeze before letting go.")
        sleep(0.8)
        print("'King and recognized true demon! I can even be summoned by the living world if they wanted to, but I don't think 'volatile, crazed explosion demon' is exactly bait for the weirdos who wanna...have fun. Anyway...'")
        print("Please press Y and then N twice.")
        continuestory = input()
        if continuestory == "Y":
            print("Thank you, something in the code was being funny.")
        else:
            print("Bruh. Alright, restart it is :) Douche.")
            break
    if path2 == "B":
        print("Johnny gives you a shove back, his lips curling up to reveal an angered toothy grin, the tall bouncer standing directly behind you. 'It wasn't my fucking fault! You didn't even want to leave your house just because it was dangerous, whilst we both know you could delete half of the world with one palm. Forget it, if you behave like this to your friends, you'd just make this whole operation a liability to our existence. And sadly, you are also a liability now.' And with that, the bouncer's hands obscure your view, one last cracking sound before the world goes dark.")
        print("Is this how you behave to your friends? Damn...guess you're in luck that murder is illegal. So you want to play again? Please type Y or N.")
        again2 = input()
        if again2 == "Y":
            print("Good luck and try not to be such a dick.")
        if again2 == "N":
            break
    if path2 == "C":
        print("Johnny's arms stayed around your waist for a while, his red aviators blocking out how his eyes stared straight (get it?) back at you, but you knew that Johnny was looking with you with nothing but the feeling of pure love in his soul. 'Wouldn't mind that to be quite honest. How about it?'")
        print("A. 'Reign over these assholes while cuddled up with you? Sounds like a dream, count me in.'")
        print("B. 'It sounds pretty perfect Johnny but I can't, you called me here to do something and I think I'm still supposed to do that for our safety. So what is it?'")    
    pathJohn = input()
    if pathJohn == "A":
        print("So it's decided. Johnny's smile was wider than you've ever seen before, tears rolling down his cheeks before he pulls you back into a tight hug, holding you and not letting go for quite a while.")
        sleep(1.5)
        print("You've become King of the Deveria, a ruling body in the land of anarchy. Every attempt on your or Johnny's life was quickly dealt with by your conjoined powers. But this is not what you were called in for...What could that have been? So, would you like to play again? Or would you like to keep Johnny and Tichettio together?")
        print("A. Tichettio deserves to be happy, a life that Johnny could give him. I want to keep them here, as the kings.")
        print("B. As much as Johnny and Tichettio could be the best kings, I want to know what Tichettio's purpose is.")
    thefuture = input()
    if thefuture == "A":
        print("You have a heart of gold. Thank you for not pulling me- I mean, Tichettio away from Johnny.")
        break
    if thefuture == "B":
        print("Completely understandable. Good luck then. Oh and Johnny says 'go fuck yourself.' What a dick huh? ;)")
        break
    print("'You're an exception to most Deverias, well, basically all of them except for me and our lovely bodyguard Rivet over there. We can travel between worlds as we please, as long as we know how to. Any Deveria who tries to do it without being allowed...simply can't do it. What, you expected me to say they explode or something?'")
    sleep(1.4)
    print("'Can't say I expected it but it would've made sense. But...' You took a moment to realize what Johnny said, taking a deep breath and slowly exhaling, a hint of smoke escaping your nostrils. 'Okay I get ya. So what am I supposed to do...wherever you're gonna send me to?'")
    sleep(1.4)
    print("'You'll be going to Earth to...well, investigate. The Quissers are helping them, those fuckin' halo wearing pieces of-' Johnny growled lightly, light explosions coming from his finger tips as he moved them a bit weirdly. 'Basically, you need to see what their plan is. Insider told me that humanity is on a downfall whilst those Quissers are up on their high and mighty thrones, not giving one single shit.'")
    sleep(1.4)
    print("'So basically you want me to go to this insider and ask around? Sounds like a plan, but one issue. I'm not a fuckin' idiot. I know Quissers can delete us as quickly as we can delete them. What's stopping them from attacking me as I arrive? Dystopia like that sounds like it would have at least 30 cameras on one street alone.'")
    sleep(1.4)
    print("'That's not an issue. Word is that the Quissers are in some icy castle of their own making, that humans constantly try to get to and then die some immensely painful death halfway through. Your natural heat and ability to light whatever on fire should keep you safe from that. As for the Quissers attacking you, beware of the insider. He's trustworthy, yes, but physical touch can leave nasty burn marks. So...will you do it?'")
    sleep(1.4)
    print("A. You refuse Johnny's offer to go to Earth, thinking that even if you get there, it will be an instant death. Johnny nods and lets you out.")
    print("B. You tell Johnny you need to think about it. It's not an everyday situation after all. Johnny nods and lets you out.")
    print("C. You accept Johnny's offer to go to Earth. You're powerful, you know your own weaknesses and you'll let nobody take you down.")
    path3 = input()
    if path3 == "A":
        print("As you follow Rivet to the world back outside, you stand there, Rivet putting a hand on your shoulder. 'Not too late to change your mind. Is this really where you want to live, awaiting that one moment someone gets you when you don't expect it?' Rivet leaves you to think, making quite a lot of sense. It's probably safer to live on Earth as a demon than down here with these insane demons ready to blow you up whenever they can. So what's it gonna be?")
        sleep(0.8)
        print("A. You decide that this is indeed what you want. Die here or die up there, at least you can die with Johnny near you.")
        sleep(0.8)
        print("B. You sigh and turn back, seeing Rivet ready to bring you back over. Guess Rivet also knows you better than you knew yourself.")
    path4 = input()
    if path4 == "A":
            print("You step outside and sit on the stairs in front of the heavy armoured door, shutting violently behind you. Well, this is it then. You can't leave this demonic hellscape. You lay down and close your eyes, hearing footsteps before your mind goes blank, going dark and never becoming light again. The end.")
            sleep(0.8)
            print("Looks like you really don't want to leave this place. If you already got this far, you must've gotten at least one bad ending so far, so you know this place is horrible! Ugh, whatever. You want to try again? Y or N please, you know the deal.")
    again4 = input()
    if again4 == "Y":
            print("Good luck")
    if again4 == "N":
        break
    if path4 == "B":
            print("You follow Rivet back to Johnny and nod your head, to which he nods back.")
            
    