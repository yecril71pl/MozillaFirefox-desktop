#
# spec file for package mozilla-xulrunner22
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#               2006-2011 Wolfgang Rosenauer
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild


Name:           mozilla-xulrunner22
BuildRequires:  autoconf213 gcc-c++ libcurl-devel libgnomeui-devel libidl-devel libnotify-devel python startup-notification-devel zip pkg-config fdupes hunspell-devel yasm Mesa-devel nss-shared-helper-devel
# needed for brp-check-bytecode-version (jar, fastjar would do as well)
BuildRequires:  unzip
%if %suse_version > 1110
BuildRequires:  libiw-devel
BuildRequires:  libproxy-devel
%else
BuildRequires:  wireless-tools
%endif
License:        MPLv1.1 or GPLv2+ or LGPLv2+
Version:        2.2a
Release:        1
%define         releasedate 2011041100
%define         version_internal 2.2a1pre
%define         apiversion 2.2
%define         uaweight 220000
Summary:        Mozilla Runtime Environment 2.2
Url:            http://www.mozilla.org
Group:          Productivity/Other
Provides:       gecko22
# this is needed to match this package with the kde4 helper package without the main package
# having a hard requirement on the kde4 package
%define kde_helper_version 6
Provides:       mozilla-kde4-version = %{kde_helper_version}
%ifarch %ix86
Provides:       mozilla-xulrunner22-32bit = %{version}-%{release}
%endif
Source:         xulrunner-source-%{version}.tar.bz2
Source1:        l10n-%{version}.tar.bz2
Source2:        find-external-requires.sh
Source3:        %{name}-rpmlintrc
Source4:        xulrunner-openSUSE-prefs.js
Source5:        add-plugins.sh.in
Source6:        create-tar.sh
Source7:        baselibs.conf
Source8:        toolkit-lockdown.js
Source9:        compare-locales.tar.bz2
Patch1:         toolkit-download-folder.patch
Patch2:         mozilla-pkgconfig.patch
Patch3:         idldir.patch
Patch4:         mozilla-nongnome-proxies.patch
Patch5:         mozilla-prefer_plugin_pref.patch
Patch6:         mozilla-shared-nss-db.patch
Patch7:         mozilla-kde.patch
Patch8:         mozilla-cairo-lcd.patch
# PATCH-FEATURE-SLED FATE#302023, FATE#302024
Patch9:         mozilla-gconf-backend.patch
Patch10:         gecko-lockdown.patch
Patch11:        toolkit-ui-lockdown.patch
# ---
Patch12:        mozilla-cpuid.patch
Patch13:        mozilla-language.patch
Patch14:        mozilla-gio.patch
Patch15:        mozilla-cairo-return.patch
Patch16:        mozilla-ntlm-full-path.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       mozilla-js22 = %{version}
Requires(post):  update-alternatives coreutils
Requires(preun): update-alternatives coreutils
### build configuration ###
%define has_system_nspr  1
%define has_system_nss   1
%define has_system_cairo 0
%define localize 1
%ifarch ppc ppc64 s390 s390x ia64
%define crashreporter    0
%define plugincontainer  0
%else
%define crashreporter    1
%define plugincontainer  1
%endif
### configuration end ###
%define _use_internal_dependency_generator 0
%define __find_requires sh %{SOURCE2}
%global provfind sh -c "grep -Ev 'mozsqlite3|dbusservice|unixprint' | %__find_provides"
%global __find_provides %provfind
%if %has_system_nspr
BuildRequires:  mozilla-nspr-devel
Requires:       mozilla-nspr >= %(rpm -q --queryformat '%{VERSION}' mozilla-nspr)
%endif
%if %has_system_nss
BuildRequires:  mozilla-nss-devel >= 3.12.8
Requires:       mozilla-nss >= %(rpm -q --queryformat '%{VERSION}' mozilla-nss)
%endif
Recommends:     %{name}-gnome

%description
XULRunner is a single installable package that can be used to bootstrap
multiple XUL+XPCOM applications that are as rich as Firefox and
Thunderbird.


%package -n mozilla-js22
License:        MPLv1.1 or GPLv2+ or LGPLv2+
Summary:        Mozilla JS 1.8.5 engine
Group:          Productivity/Other

%description -n mozilla-js22
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscape's JavaScript is a
superset of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.


%package devel
License:        MPLv1.1 or GPLv2+ or LGPLv2+
Summary:        XULRunner/Gecko SDK 2.0
Group:          Development/Libraries/Other
%if %has_system_nspr
Requires:       mozilla-nspr-devel >= %(rpm -q --queryformat '%{VERSION}' mozilla-nspr-devel)
%endif
%if %has_system_nss
Requires:       mozilla-nss-devel >= %(rpm -q --queryformat '%{VERSION}' mozilla-nss-devel)
%endif
Requires:       %{name} = %{version}

%description devel
Software Development Kit to embed XUL or Gecko into other applications.

%if %localize

%package translations-common
License:        MPLv1.1 or GPLv2+ or LGPLv2+
Summary:        Common translations for XULRunner 2.0
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ar;ca;cs;da;de;en_GB;es_AR;es_CL;es_ES;fi;fr;hu;it;ja;ko;nb_NO;nl;pl;pt_BR;pt_PT;ru;sv_SE;zh_CN;zh_TW)
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-common
XULRunner is a single installable package that can be used to bootstrap
multiple XUL+XPCOM applications that are as rich as Firefox and
Thunderbird.

This package contains the most common languages but en-US which is
delivered in the main package.


%package translations-other
License:        MPLv1.1 or GPLv2+ or LGPLv2+
Summary:        Extra translations for XULRunner 2.0
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:af;ak;ast;be;bg;bn_BD;br;bs;cy;el;en_ZA;eo;es_MX;et;eu;fa;fy_NL;ga_IE;gd;gl;gu_IN;he;hi_IN;hr;hy_AM;id;is;kk;kn;ku;lg;lt;lv;mai;mk;ml;mr;nn_NO;nso;or;pa_IN;rm;ro;si;sk;sl;son;sq;sr;ta;ta_LK;te;th;tr;uk;zu)
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-other
XULRunner is a single installable package that can be used to bootstrap
multiple XUL+XPCOM applications that are as rich as Firefox and
Thunderbird.

This package contains rarely used languages.
%endif

%package gnome
License:        MPLv1.1 or GPLv2+ or LGPLv2+
Summary:        XULRunner components depending on gnome-vfs
Group:          Productivity/Other
Requires:       %{name} = %{version}-%{release}
Requires(post): coreutils

%description gnome
This subpackage contains the Gnome components which rely on certain
Gnome subsystems to be installed. They are recommended for full
desktop integration but not mandatory for small disk footprint
KDE installations for example.


%if %crashreporter
%package buildsymbols
License:        MPLv1.1 or GPLv2+ or LGPLv2+
Summary:        Breakpad buildsymbols for %{name}
Group:          Development/Debug

%description buildsymbols
This subpackage contains the Breakpad created and compatible debugging
symbols meant for upload to Mozilla's crash collector database.
%endif

%prep
%setup -n mozilla -q -b 1 -b 9
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
#%patch9 -p1
#%patch10 -p1
#%patch11 -p1
%if %suse_version < 1120
#%patch12 -p1
%endif
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
kdehelperversion=$(cat toolkit/xre/nsKDEUtils.cpp | grep '#define KMOZILLAHELPER_VERSION' | cut -d ' ' -f 3)
if test "$kdehelperversion" != %{kde_helper_version}; then
  echo fix kde helper version in the .spec file
  exit 1
fi
source other-licenses/branding/firefox/configure.sh
unset MOZ_APP_DISPLAYNAME
export MOZ_UA_BUILDID
MOZ_APP_DIR=%{_libdir}/xulrunner-%{version_internal}
export MOZ_BUILD_DATE=%{releasedate}
export CFLAGS="$RPM_OPT_FLAGS -Os -fno-strict-aliasing"
%ifarch ppc64
export CFLAGS="$CFLAGS -mminimal-toc"
%endif
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-Wl,-rpath -Wl,${MOZ_APP_DIR}"
export MOZCONFIG=$RPM_BUILD_DIR/mozconfig
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1
export MOZ_MILESTONE_RELEASE=1
#
cat << EOF > $MOZCONFIG
mk_add_options MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZ_MILESTONE_RELEASE=1
mk_add_options MOZ_MAKE_FLAGS=%{?jobs:-j%jobs}
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/../obj
. \$topsrcdir/xulrunner/config/mozconfig
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --sysconfdir=%{_sysconfdir}
ac_add_options --mandir=%{_mandir}
ac_add_options --includedir=%{_includedir}
ac_add_options --enable-optimize
ac_add_options --enable-extensions=default
#ac_add_options --with-system-jpeg # mozilla uses internal libjpeg-turbo now
#ac_add_options --with-system-png  # no APNG support
ac_add_options --with-system-zlib
ac_add_options --with-l10n-base=../l10n
ac_add_options --disable-tests
ac_add_options --disable-mochitest
ac_add_options --disable-installer
ac_add_options --disable-updater
ac_add_options --disable-javaxpcom
ac_add_options --enable-startup-notification
ac_add_options --enable-url-classifier
ac_add_options --enable-system-hunspell
ac_add_options --enable-shared-js
#ac_add_options --enable-debug
EOF
%if %suse_version > 1130
cat << EOF >> $MOZCONFIG
ac_add_options --disable-gnomevfs
ac_add_options --enable-gio
EOF
%endif
%if %has_system_nspr
cat << EOF >> $MOZCONFIG
ac_add_options --with-system-nspr
EOF
%endif
%if %has_system_nss
cat << EOF >> $MOZCONFIG
ac_add_options --with-system-nss
EOF
%endif
%if %has_system_cairo
cat << EOF >> $MOZCONFIG
ac_add_options --enable-system-cairo
EOF
%endif
%if %suse_version > 1110
cat << EOF >> $MOZCONFIG
ac_add_options --enable-libproxy
EOF
%endif
%if ! %crashreporter
cat << EOF >> $MOZCONFIG
ac_add_options --disable-crashreporter
EOF
%endif
%if ! %plugincontainer
cat << EOF >> $MOZCONFIG
# Chromium IPC is not ported to Power,S/390 and Itanium (currently just x86,x86_64 and arm)
ac_add_options --disable-ipc
EOF
%endif
make -f client.mk build

%install
cd ../obj
%makeinstall STRIP=/bin/true
# remove some executable permissions
find $RPM_BUILD_ROOT%{_includedir}/xulrunner-%{version_internal} \
     -type f -perm -111 -exec chmod a-x {} \;
find $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/ \
     -name "*.js" -o -name "*.xpm" -o -name "*.png" | xargs chmod a-x
mkdir -p $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/extensions
# fixing SDK dynamic libs (symlink instead of copy)
rm $RPM_BUILD_ROOT%{_libdir}/xulrunner-devel-%{version_internal}/sdk/lib/*.so
ln -sf ../../../xulrunner-%{version_internal}/libmozjs.so \
       $RPM_BUILD_ROOT%{_libdir}/xulrunner-devel-%{version_internal}/sdk/lib/
ln -sf ../../../xulrunner-%{version_internal}/libxpcom.so \
       $RPM_BUILD_ROOT%{_libdir}/xulrunner-devel-%{version_internal}/sdk/lib/
ln -sf ../../../xulrunner-%{version_internal}/libxul.so \
       $RPM_BUILD_ROOT%{_libdir}/xulrunner-devel-%{version_internal}/sdk/lib/
# include basic buildenv for xulapps to use
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xulrunner-%{version_internal}
pushd ..
# this list has been compiled by trial and error for prism
tar --exclude=*.cpp --exclude=*.mm \
   -cvjf $RPM_BUILD_ROOT%{_datadir}/xulrunner-%{version_internal}/mozilla-src.tar.bz2 \
    mozilla/configure.in mozilla/Makefile.in mozilla/client.py mozilla/allmakefiles.sh \
    mozilla/config mozilla/client.mk mozilla/aclocal.m4 mozilla/build mozilla/js/src/* \
    mozilla/testing mozilla/toolkit/mozapps/installer mozilla/probes mozilla/memory \
    mozilla/toolkit/xre mozilla/nsprpub/config mozilla/tools mozilla/xpcom/build
popd
# XPI example
#cp -rL dist/xpi-stage/simple $RPM_BUILD_ROOT/%{_libdir}/xulrunner-%{version_internal}/
# preferences
cp %{SOURCE4} $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/defaults/pref/all-openSUSE.js
cp %{SOURCE8} $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/defaults/pref/lockdown.js
# install add-plugins.sh
sed "s:%%PROGDIR:%{_libdir}/xulrunner-%{version_internal}:g" \
  %{SOURCE5} > $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/add-plugins.sh
chmod 755 $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/add-plugins.sh
# ghosts
touch $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/global.reginfo
# install additional locales
%if %localize
rm -f %{_tmppath}/translations.*
touch %{_tmppath}/translations.{common,other}
for locale in $(awk '{ print $1; }' ../mozilla/browser/locales/shipped-locales); do
  case $locale in
   ja-JP-mac|en-US|bn-IN)
      ;;
   *)
      pushd $RPM_BUILD_DIR/compare-locales
      PYTHONPATH=lib \
        scripts/compare-locales -m ../l10n-merged/$locale \
	../mozilla/toolkit/locales/l10n.ini ../l10n $locale
      popd
      LOCALE_MERGEDIR=../l10n-merged \
      make -C toolkit/locales libs-$locale
      cp dist/xpi-stage/locale-$locale/chrome/$locale.jar \
         $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/chrome
      cp dist/xpi-stage/locale-$locale/chrome/$locale.manifest \
         $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/chrome
      # check against the fixed common list and sort into the right filelist
      _matched=0
      for _match in ar ca cs da de en-GB es-AR es-CL es-ES fi fr hu it ja ko nb-NO nl pl pt-BR pt-PT ru sv-SE zh-CN zh-TW; do
        [ "$_match" = "$locale" ] && _matched=1
      done
      [ $_matched -eq 1 ] && _l10ntarget=common || _l10ntarget=other
      echo %{_libdir}/xulrunner-%{version_internal}/chrome/$locale.jar \
         >> %{_tmppath}/translations.$_l10ntarget
      echo %{_libdir}/xulrunner-%{version_internal}/chrome/$locale.manifest \
         >> %{_tmppath}/translations.$_l10ntarget
  esac
done
%endif
# API symlink
ln -sf xulrunner-%{version_internal} $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{apiversion}
# compat links
%if 0%{?ga_version:1}
touch $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{ga_version}
%endif
# excludes
%if %suse_version < 1120
rm -f $RPM_BUILD_ROOT%{_bindir}/xulrunner
%endif
rm -f $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/updater
rm -f $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/update.locale
rm -f $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/LICENSE
rm -f $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/README.txt
rm -f $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/dictionaries/en-US*
rm -f $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/nspr-config
# fdupes
%fdupes $RPM_BUILD_ROOT%{_includedir}/xulrunner-%{version_internal}/
%fdupes $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/
# create breakpad debugsymbols
%if %crashreporter
SYMBOLS_NAME="xulrunner-%{version}-%{release}.%{_arch}-%{suse_version}-symbols"
make buildsymbols \
  SYMBOL_INDEX_NAME="$SYMBOLS_NAME.txt" \
  SYMBOL_FULL_ARCHIVE_BASENAME="$SYMBOLS_NAME-full" \
  SYMBOL_ARCHIVE_BASENAME="$SYMBOLS_NAME"
if [ -e dist/*symbols.zip ]; then
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/mozilla/
  cp dist/*symbols.zip $RPM_BUILD_ROOT%{_datadir}/mozilla/
fi
%endif

%clean
rm -rf $RPM_BUILD_ROOT
%if %localize
rm -rf %{_tmppath}/translations.*
%endif

%post
/usr/sbin/update-alternatives --install %{_bindir}/xulrunner \
  xulrunner %{_libdir}/xulrunner-%{apiversion}/xulrunner %{uaweight} || :
%{_libdir}/xulrunner-%{apiversion}/add-plugins.sh > /dev/null 2>&1
exit 0

%posttrans
# needed for updates which transition directory to symlink
%if 0%{?ga_version:1}
test -d %{_libdir}/xulrunner-%{ga_version} && rm -rf %{_libdir}/xulrunner-%{ga_version}
ln -sf xulrunner-%{version_internal} %{_libdir}/xulrunner-%{ga_version}
%endif
[ -e %{_libdir}/xulrunner-%{version_internal}/add-plugins.sh ] && \
  %{_libdir}/xulrunner-%{version_internal}/add-plugins.sh > /dev/null 2>&1
exit 0

%preun
if [ "$1" = "0" ]; then # deinstallation
  # that's not quite nice since old versions should be removed on update as well
  # but that's problematic for updates w/o raising the version number
  /usr/sbin/update-alternatives --remove xulrunner %{_libdir}/xulrunner-%{apiversion}/xulrunner
fi
rm -f %{_libdir}/xulrunner-%{version_internal}/dictionaries/*
exit 0

%triggerin -- myspell-dictionary
%{_libdir}/xulrunner-%{version_internal}/add-plugins.sh > /dev/null 2>&1
exit 0

%triggerpostun -- myspell-dictionary
%{_libdir}/xulrunner-%{version_internal}/add-plugins.sh > /dev/null 2>&1
exit 0

%files
%defattr(-,root,root)
%dir %{_libdir}/xulrunner-%{version_internal}/
%dir %{_libdir}/xulrunner-%{version_internal}/chrome/
%dir %{_libdir}/xulrunner-%{version_internal}/dictionaries/
%dir %{_libdir}/xulrunner-%{version_internal}/extensions/
%{_libdir}/xulrunner-%{version_internal}/chrome/en-US.*
%{_libdir}/xulrunner-%{version_internal}/chrome/pippki.*
%{_libdir}/xulrunner-%{version_internal}/chrome/toolkit.*
%{_libdir}/xulrunner-%{version_internal}/chrome/icons/
%{_libdir}/xulrunner-%{version_internal}/components/
%exclude %{_libdir}/xulrunner-%{version_internal}/components/libmozgnome.so
%if %suse_version <= 1130
%exclude %{_libdir}/xulrunner-%{version_internal}/components/libnkgnomevfs.so
%endif
%{_libdir}/xulrunner-%{version_internal}/defaults/
%{_libdir}/xulrunner-%{version_internal}/greprefs.js
%{_libdir}/xulrunner-%{version_internal}/icons/
%{_libdir}/xulrunner-%{version_internal}/modules/
%{_libdir}/xulrunner-%{version_internal}/plugins/
%{_libdir}/xulrunner-%{version_internal}/res/
%{_libdir}/xulrunner-%{version_internal}/*.so
%exclude %{_libdir}/xulrunner-%{version_internal}/libmozjs.so
%{_libdir}/xulrunner-%{version_internal}/add-plugins.sh
%{_libdir}/xulrunner-%{version_internal}/chrome.manifest
%{_libdir}/xulrunner-%{version_internal}/dependentlibs.list
%{_libdir}/xulrunner-%{version_internal}/mozilla-xremote-client
%if %plugincontainer
%{_libdir}/xulrunner-%{version_internal}/plugin-container
%endif
%{_libdir}/xulrunner-%{version_internal}/run-mozilla.sh
%{_libdir}/xulrunner-%{version_internal}/xulrunner
%{_libdir}/xulrunner-%{version_internal}/xulrunner-bin
%{_libdir}/xulrunner-%{version_internal}/xulrunner-stub
%{_libdir}/xulrunner-%{version_internal}/platform.ini
# crashreporter files
%if %crashreporter
%{_libdir}/xulrunner-%{version_internal}/crashreporter
%{_libdir}/xulrunner-%{version_internal}/crashreporter.ini
%{_libdir}/xulrunner-%{version_internal}/Throbber-small.gif
%endif
# ghosts
%ghost %{_libdir}/xulrunner-%{version_internal}/global.reginfo
%if %suse_version >= 1120
%ghost %{_bindir}/xulrunner
%endif
# API symlink
%{_libdir}/xulrunner-%{apiversion}
# compat symlinks
%if 0%{?ga_version:1}
%ghost %{_libdir}/xulrunner-%{ga_version}
%endif

%files -n mozilla-js22
%defattr(-,root,root)
%dir %{_libdir}/xulrunner-%{version_internal}/
%{_libdir}/xulrunner-%{apiversion}
%{_libdir}/xulrunner-%{version_internal}/libmozjs.so

%files devel
%defattr(-,root,root)
%{_libdir}/xulrunner-%{version_internal}/xpcshell
%{_libdir}/xulrunner-%{version_internal}/xpidl
%{_libdir}/xulrunner-%{version_internal}/xpt_dump
%{_libdir}/xulrunner-%{version_internal}/xpt_link
%{_libdir}/xulrunner-devel-%{version_internal}/
# FIXME symlink dynamic libs below sdk/lib
%attr(644,root,root) %{_libdir}/pkgconfig/*
%{_includedir}/xulrunner-%{version_internal}/
%{_datadir}/xulrunner-%{version_internal}/

%files gnome
%defattr(-,root,root)
%dir %{_libdir}/xulrunner-%{version_internal}/
%dir %{_libdir}/xulrunner-%{version_internal}/components/
%{_libdir}/xulrunner-%{version_internal}/components/libmozgnome.so
%if %suse_version <= 1130
%{_libdir}/xulrunner-%{version_internal}/components/libnkgnomevfs.so
%endif

%if %localize
%files translations-common -f %{_tmppath}/translations.common
%defattr(-,root,root)
%dir %{_libdir}/xulrunner-%{version_internal}/
%dir %{_libdir}/xulrunner-%{version_internal}/chrome/

%files translations-other -f %{_tmppath}/translations.other
%defattr(-,root,root)
%dir %{_libdir}/xulrunner-%{version_internal}/
%dir %{_libdir}/xulrunner-%{version_internal}/chrome/
%endif

%if %crashreporter
%files buildsymbols
%defattr(-,root,root)
%{_datadir}/mozilla/
%endif

%changelog