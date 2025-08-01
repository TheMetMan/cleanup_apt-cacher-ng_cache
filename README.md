# cleanup_apt-cacher-ng_cache
## Script to Cleanup Apt Cacher NG Cache on Gentoo Linux
**apt-cacher-ng** package is a way of creating a **[Local Distfiles Cache](https://wiki.gentoo.org/wiki/Local_distfiles_cache)**. This package has a cron job to clean up wasted space which does not work.</br>
Having read about this on the Gentoo Linux forum **[here](https://forums.gentoo.org/viewtopic-p-8770951.html)**, I also decided to write a Python Script to run after my updates to clean the cache and save space.</br>
I had a situation where the **var** partion was 90% full. This was caused by the **apt-cacher-ng** package leaving unnecessary files lying about.</br>
When I ran the script it deleted well over 1000 files, I recovered 57Gb of space leaving the partition at only 9% full. RESULT!</br>
