define E = Character("ellen ", color="#678CD1")
define F = Character("felex", color="#C77850")

label another_script:

  E "Hello, {color=#C77850}(#{/color}{color=#C77850}C77850{/color}{color=#C77850})what {/color}is up ??"
  F "its good"
  "And so the {size=+15}introduction {/size}was set on plan"
# idk if this will work or not
# but just for something i guess it will be good
  E "what will you choose ?"
  menu:
    "go left":
      jump left_scene

label left_scene:
  E "oh my godd"
  "{color=#AB5B9A}(#{/color}{color=#AB5B9A}AB5B9A{/color}{color=#AB5B9A}) Elly{/color}: what happened ?"
