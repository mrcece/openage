# openage main makefile
#
# this actually just forwards calls to the cmake-generated files in bin.


# original msage2 asset directory
AGE2DIR=

# openage asset directory
DATADIR=data

# this list specifies needed media files for the convert script
# TODO: don't rely on the make system, let our binary call the convert script
needed_media = graphics:*.* terrain:*.* sounds0:*.* sounds1:*.* gamedata0:*.* gamedata1:*.* gamedata2:*.* interface:*.*

binary = ./openage
runargs = --data=$(DATADIR)
BUILDDIR = bin

.PHONY: all
all: openage

$(BUILDDIR):
	@echo "call ./configure to initialize the build directory."
	@echo "also see ./configure --help, and building.md"
	@echo ""
	@false

.PHONY: openage
openage: $(BUILDDIR)
	@make -C $(BUILDDIR)

.PHONY: install
install: $(BUILDDIR)
	@make -C $(BUILDDIR) install

.PHONY: media
media: $(BUILDDIR)
	@if test ! -d "$(AGE2DIR)"; then echo "you need to specify AGE2DIR (e.g. ~/.wine/drive_c/age)."; false; fi
	buildsystem/runinenv PYTHONPATH=prependpath:py python3 -m openage.convert -v media -o "$(DATADIR)/age/" "$(AGE2DIR)" $(needed_media)

.PHONY: medialist
medialist:
	@echo "$(needed_media)"

.PHONY: run
run: openage
	$(binary) $(runargs)

.PHONY: runval
runval: openage
	valgrind --leak-check=full --track-origins=yes -v $(binary) $(runargs)

.PHONY: rungdb
rungdb: openage
	gdb --args $(binary) $(runargs)

.PHONY: test
test: $(BUILDDIR)
	@make -C $(BUILDDIR) test

.PHONY: codegen
codegen: $(BUILDDIR)
	@make -C $(BUILDDIR) codegen

.PHONY: doc
doc: $(BUILDDIR)
	@make -C $(BUILDDIR) doc

.PHONY: clean
clean: $(BUILDDIR)
	# removes all objects and binaries
	@make -C $(BUILDDIR) clean

.PHONY: cleanbin
cleanbin:
	@echo build directories
	rm -rf .bin
	@echo symlinks
	rm -rf openage bin
	@echo remains from accidential in-source builds
	rm -rf CMakeCache.txt CMakeFiles cmake_install.cmake

.PHONY: mrproper
mrproper: cleanbin
	@echo converted assets
	rm -rf $(DATADIR)/age

.PHONY: help
help: $(BUILDDIR)/Makefile
	@echo "openage buildsystem"
	@echo ""
	@echo ""
	@echo ""
	@echo "targets:"
	@echo ""
	@echo "openage   -> compile main binary"
	@echo "media     -> convert media files, usage: make media AGE2DIR=~/.wine/ms-games/age2"
	@echo "medialist -> list needed media files for current version"
	@echo "doc       -> create documentation files"
	@echo ""
	@echo "clean     -> clean up object files"
	@echo "cleanbin  -> clean up all files generated by ./configure and make"
	@echo "mrproper  -> additionally delete converted assets
	@echo ""
	@echo "run       -> run openage"
	@echo "runval    -> run valgrind, analyze for memleaks"
	@echo "rungdb    -> run inside gdb"
	@echo ""
	@echo ""
	@echo "Now follows the CMake help. (= make -C $(BUILDDIR)) :"
	@make -C $(BUILDDIR) help