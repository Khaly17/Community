const toggleSwitch = document.querySelector('input[type = "checkbox"]');
const doc = document.getElementsByTagName('html')[0];
const bg = document.getElementById('torch');



// On page load or when changing themes, best to add inline in `head` to avoid FOUC
if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    doc.className = 'dark'
    bg.className = "bg-black dark:bg-black"


    toggleSwitch.checked = true;
  } else {
    doc.className = 'light'
    bg.className = "bg-white dark:bg-black"

    //document.documentElement.classList.remove('dark')
  }

  function switchTheme(){
      if(toggleSwitch.checked){
        localStorage.setItem('theme','dark');
        doc.className = 'dark'
        bg.className = "bg-black dark:bg-black"
      }
      else{
        localStorage.setItem('theme','light');
        doc.className = 'light'
        bg.className = "bg-white dark:bg-black"
      }
  }


  toggleSwitch.addEventListener('click',switchTheme,false);

