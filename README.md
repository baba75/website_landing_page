Website Landing Page
====================

Landing pages are web pages designed to collect leads from a specific campaign. The customer clicks on a link from a specific email or advertising and arrives in the landing page—the landing page act as a funnel to collect leads. 
It is important that the user can exit the page only by compiling a form or by making the action designed.
For this reason, it is important to remove all the links that can distract the user, creating a no-escape page.
This module installs a layout template without the logo, the menu and the footer.

Configuration
-------------
Create the landing page with the web editor, as usual, then you can find it as a view in Settings/Views menu. (You need to activate the developer mode)
Open the view corresponding to the page, and substitute the call to:

&lt;t t-call="website.layout"&gt;

with

&lt;t t-call="website_landing_page.layout"&gt;

Enter the page from the browser, from the customize menu you can activate/deactivate the landing page mode.

Bug Tracker
===========

Bugs are tracked on GitHub Issues <https://github.com/baba75/website_landing_page/issues>. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing detailed and welcomed feedback.


Credits
=======

Mantainer
------------
* Alberto Carollo <baba75@gmail.com>

