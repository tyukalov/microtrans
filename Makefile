 #    This program is free software: you can redistribute it and/or modify
 #    it under the terms of the GNU General Public License as published by
 #    the Free Software Foundation, either version 3 of the License, or
 #    (at your option) any later version.

 #    This program is distributed in the hope that it will be useful,
 #    but WITHOUT ANY WARRANTY; without even the implied warranty of
 #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #    GNU General Public License for more details.

 #    You should have received a copy of the GNU General Public License
 #    along with this program.  If not, see <http://www.gnu.org/licenses/>.

 # Igor Tyukalov <tyukalov@bk.ru> 

langx:
	xgettext --keyword=_ --language=Python --add-comments --sort-output -o lang/$(NAME).pot ./*.py
	msginit --input=lang/$(NAME).pot --locale=ru --output=lang/$(NAME).po
langinstall:
	msgfmt --output-file=lang/ru/LC_MESSAGES/microtrans.mo lang/microtrans.po
langmerge:
	msgmerge --backup=none -U lang/microtrans.po lang/$(NAME).po
	rm lang/$(NAME).po lang/$(NAME).pot

