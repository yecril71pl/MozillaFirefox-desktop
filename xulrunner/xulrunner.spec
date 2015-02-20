#
# spec file for package xulrunner
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#               2006-2015 Wolfgang Rosenauer
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


%define version_internal 31.5.0
%define apiversion 31
%define uaweight 3150000
%define releasedate 2015021900
%define shared_js 0
%define has_system_nspr  1
%define has_system_nss   1
%define has_system_cairo 0
%define localize         0
%ifarch aarch64 ppc ppc64 ppc64le s390 s390x ia64 %arm
%define crashreporter    0
%else
%define crashreporter    0
%endif
%if %suse_version > 1210
%if %suse_version > 1310
%define gstreamer_ver 1.0
%define gstreamer 1
%else
%define gstreamer_ver 0.10
%endif
%endif

Name:           xulrunner
BuildRequires:  Mesa-devel
BuildRequires:  autoconf213
BuildRequires:  dbus-1-glib-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  libidl-devel
BuildRequires:  libnotify-devel
%if %suse_version > 1140
BuildRequires:  makeinfo
%endif
BuildRequires:  pkg-config
BuildRequires:  python
BuildRequires:  startup-notification-devel
BuildRequires:  unzip
BuildRequires:  xorg-x11-libXt-devel
BuildRequires:  yasm
BuildRequires:  zip
%if %suse_version > 1110
BuildRequires:  libiw-devel
BuildRequires:  libproxy-devel
%else
BuildRequires:  wireless-tools
%endif
BuildRequires:  mozilla-nspr-devel >= 4.10.6
BuildRequires:  mozilla-nss-devel >= 3.16.5
BuildRequires:  pkgconfig(libpulse)
%if %suse_version > 1210
BuildRequires:  pkgconfig(gstreamer-%gstreamer_ver)
BuildRequires:  pkgconfig(gstreamer-app-%gstreamer_ver)
BuildRequires:  pkgconfig(gstreamer-plugins-base-%gstreamer_ver)
%if 0%{?gstreamer} == 1
Requires:       libgstreamer-1_0-0
Recommends:     gstreamer-fluendo-mp3
Recommends:     gstreamer-plugin-libav
%else
Requires:       libgstreamer-0_10-0
Recommends:     gstreamer-0_10-fluendo-mp3
Recommends:     gstreamer-0_10-plugins-ffmpeg
%endif
%endif
Version:        %{version_internal}
Release:        0
Summary:        Mozilla Runtime Environment
License:        MPL-2.0
Group:          Productivity/Other
Url:            http://www.mozilla.org/
Provides:       gecko
%ifarch %ix86
Provides:       xulrunner-32bit = %{version}-%{release}
%endif
Source:         xulrunner-%{version}-source.tar.xz
Source1:        l10n-%{version}.tar.xz
Source2:        find-external-requires.sh
Source3:        %{name}-rpmlintrc
Source4:        xulrunner-openSUSE-prefs.js
Source5:        spellcheck.js
Source6:        create-tar.sh
Source7:        baselibs.conf
Source8:        source-stamp.txt
Source9:        compare-locales.tar.xz
Patch1:         toolkit-download-folder.patch
Patch2:         mozilla-nongnome-proxies.patch
Patch3:         mozilla-prefer_plugin_pref.patch
Patch4:         mozilla-pkgconfig.patch
Patch6:         mozilla-preferences.patch
Patch7:         mozilla-language.patch
Patch8:         mozilla-ntlm-full-path.patch
Patch9:         mozilla-repo.patch
Patch10:        mozilla-sle11.patch
Patch11:        mozilla-icu-strncat.patch
Patch12:        mozilla-arm-disable-edsp.patch
Patch13:        mozilla-ppc.patch
Patch14:        mozilla-libproxy-compat.patch
Patch15:        mozilla-nullptr-gcc45.patch
Patch16:        mozilla-idldir.patch
# Gecko/Toolkit AArch64 Porting
Patch30:        mozilla-aarch64-bmo-810631.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?shared_js} == 1
Requires:       mozilla-js = %{version}
%endif
Requires(post):  update-alternatives coreutils
Requires(preun): update-alternatives coreutils
Provides:       xulrunner-esr = %{version}
Obsoletes:      xulrunner-esr < 24.0
%define _use_internal_dependency_generator 0
%define __find_requires sh %{SOURCE2}
%global provfind sh -c "grep -Ev 'mozsqlite3|dbusservice|unixprint' | %__find_provides"
%global __find_provides %provfind
%if %has_system_nspr
Requires:       mozilla-nspr >= %(rpm -q --queryformat '%{VERSION}' mozilla-nspr)
%endif
%if %has_system_nss
Requires:       mozilla-nss >= %(rpm -q --queryformat '%{VERSION}' mozilla-nss)
%endif

%description
XULRunner is a single installable package that can be used to bootstrap
multiple XUL+XPCOM applications that are as rich as Firefox and
Thunderbird.

%if 0%{?shared_js} == 1
%package -n mozilla-js
Summary:        Mozilla JS engine
Group:          Productivity/Other

%description -n mozilla-js
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscape's JavaScript is a
superset of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.
%endif

%package devel
Summary:        XULRunner/Gecko SDK
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
Summary:        Common translations for XULRunner
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ar;ca;cs;da;de;el;en_GB;es_AR;es_CL;es_ES;fi;fr;hu;it;ja;ko;nb_NO;nl;pl;pt_BR;pt_PT;ru;sv_SE;zh_CN;zh_TW)
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-common
XULRunner is a single installable package that can be used to bootstrap
multiple XUL+XPCOM applications that are as rich as Firefox and
Thunderbird.

This package contains the most common languages but en-US which is
delivered in the main package.


%package translations-other
Summary:        Extra translations for XULRunner
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ach;af;ak;as;ast;be;bg;bn_BD;bn_IN;br;bs;csb;cy;en_ZA;eo;es_MX;et;eu;fa;ff;fy_NL;ga_IE;gd;gl;gu_IN;he;hi_IN;hr;hy_AM;id;is;kk;km;kn;ku;lg;lij;lt;lv;mai;mk;ml;mr;nn_NO;nso;or;pa_IN;rm;ro;si;sk;sl;son;sq;sr;ta;ta_LK;te;th;tr;uk;vi;zu)
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-other
XULRunner is a single installable package that can be used to bootstrap
multiple XUL+XPCOM applications that are as rich as Firefox and
Thunderbird.

This package contains rarely used languages.
%endif

%if %crashreporter
%package buildsymbols
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
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%if %suse_version < 1120
%patch10 -p1
%endif
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch30 -p1

%build
# no need to add build time to binaries
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +
#
MOZ_APP_DIR=%{_libdir}/xulrunner-%{version_internal}
source %{SOURCE8}
export MOZ_BUILD_DATE=%{releasedate}
export MOZ_SOURCE_STAMP=$REV
export SOURCE_REPO=$REPO
export source_repo=$REPO
export MOZ_SOURCE_REPO=$REPO
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%ifarch %ix86
export CFLAGS="${CFLAGS} -Os"
%endif
%ifarch ppc64
export CFLAGS="$CFLAGS -mminimal-toc"
%endif
export LDFLAGS=" -Wl,-rpath -Wl,${MOZ_APP_DIR}"
%ifarch %arm
# debug symbols require too much memory during build
export CFLAGS="${CFLAGS/-g / }"
# Limit RAM usage during link
LDFLAGS+="-Wl,--reduce-memory-overheads -Wl,--no-keep-memory"
%endif
export CXXFLAGS="$CFLAGS"
export MOZCONFIG=$RPM_BUILD_DIR/mozconfig
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
ac_add_options --enable-release
ac_add_options --enable-stdcxx-compat
%ifarch %ix86
%if 0%{?suse_version} > 1230
ac_add_options --disable-optimize
%endif
%endif
%ifnarch aarch64 ppc ppc64 ppc64le
ac_add_options --enable-elf-hack
%endif
ac_add_options --enable-extensions=default
#ac_add_options --with-system-jpeg # mozilla uses internal libjpeg-turbo now
#ac_add_options --with-system-png  # no APNG support
ac_add_options --with-system-zlib
ac_add_options --with-l10n-base=$RPM_BUILD_DIR/l10n
ac_add_options --disable-tests
ac_add_options --disable-mochitest
ac_add_options --disable-installer
ac_add_options --disable-updater
ac_add_options --disable-javaxpcom
ac_add_options --enable-system-hunspell
ac_add_options --enable-startup-notification
%if 0%{?shared_js} == 1
ac_add_options --enable-shared-js
%endif
#ac_add_options --enable-debug
%if %suse_version > 1130
ac_add_options --disable-gnomevfs
ac_add_options --enable-gio
%endif
%if 0%{?gstreamer} == 1
ac_add_options --enable-gstreamer=1.0
%endif
%if %suse_version < 1220
ac_add_options --disable-gstreamer
%endif
%if %has_system_nspr
ac_add_options --with-system-nspr
%endif
%if %has_system_nss
ac_add_options --with-system-nss
%endif
%if %has_system_cairo
ac_add_options --enable-system-cairo
%endif
%if %suse_version > 1110
ac_add_options --enable-libproxy
%endif
%if ! %crashreporter
ac_add_options --disable-crashreporter
%endif
# ARM
%ifarch %arm
ac_add_options --disable-neon
%endif
%ifnarch %ix86 x86_64
ac_add_options --disable-webrtc
%endif
# try to use OpenGL-ES on ARM
%ifarch %arm
ac_add_options --with-gl-provider=EGL
%endif
EOF
make -f client.mk build

%install
cd ../obj
# preferences (to package in omni.jar)
cp %{SOURCE4} dist/bin/defaults/pref/all-openSUSE.js
cp %{SOURCE5} dist/bin/defaults/pref/
%makeinstall STRIP=/bin/true
# xpt.py is not executable
chmod a+x $RPM_BUILD_ROOT%{_libdir}/xulrunner-devel-%{version_internal}/sdk/bin/*.py
# remove some executable permissions
find $RPM_BUILD_ROOT%{_includedir}/xulrunner-%{version_internal} \
     -type f -perm -111 -exec chmod a-x {} \;
find $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/ \
     -name "*.js" -o -name "*.xpm" -o -name "*.png" | xargs chmod a-x
# remove mkdir.done files from installed base
#find $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal} -name ".mkdir.done" | xargs rm
mkdir -p $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/extensions
# fixing SDK dynamic libs (symlink instead of copy)
rm $RPM_BUILD_ROOT%{_libdir}/xulrunner-devel-%{version_internal}/sdk/lib/*.so
%if 0%{?shared_js} == 1
ln -sf ../../../xulrunner-%{version_internal}/libmozjs.so \
       $RPM_BUILD_ROOT%{_libdir}/xulrunner-devel-%{version_internal}/sdk/lib/
%endif
ln -sf ../../../xulrunner-%{version_internal}/libxul.so \
       $RPM_BUILD_ROOT%{_libdir}/xulrunner-devel-%{version_internal}/sdk/lib/
# include basic buildenv for xulapps to use
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xulrunner-%{version_internal}
pushd ..
# this list has been compiled by trial and error for prism
tar --exclude=*.cpp --exclude=*.mm \
   -cvjf $RPM_BUILD_ROOT%{_datadir}/xulrunner-%{version_internal}/mozilla-src.tar.bz2 \
    mozilla/configure.in mozilla/Makefile.in mozilla/client.py \
    mozilla/config mozilla/client.mk mozilla/aclocal.m4 mozilla/build mozilla/js/src/* \
    mozilla/testing mozilla/toolkit/mozapps/installer mozilla/probes mozilla/memory \
    mozilla/toolkit/xre mozilla/nsprpub/config mozilla/tools mozilla/xpcom/build
popd
# ghosts
touch $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/global.reginfo
# install additional locales
%if %localize
rm -f %{_tmppath}/translations.*
touch %{_tmppath}/translations.{common,other}
for locale in $(awk '{ print $1; }' ../mozilla/browser/locales/shipped-locales); do
  case $locale in
   ja-JP-mac|en-US)
      ;;
   *)
      pushd $RPM_BUILD_DIR/compare-locales
      PYTHONPATH=lib \
        scripts/compare-locales -m ../l10n-merged/$locale \
	../mozilla/toolkit/locales/l10n.ini ../l10n $locale
      popd
      LOCALE_MERGEDIR=$RPM_BUILD_DIR/l10n-merged/$locale \
      make -C toolkit/locales langpack-$locale
      cp dist/xpi-stage/locale-$locale \
         $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/extensions/langpack-$locale@firefox.mozilla.org
      # remove prefs and profile defaults from langpack
      rm -rf $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/extensions/langpack-$locale@firefox.mozilla.org/defaults
      # check against the fixed common list and sort into the right filelist
      _matched=0
      for _match in ar ca cs da de el en-GB es-AR es-CL es-ES fi fr hu it ja ko nb-NO nl pl pt-BR pt-PT ru sv-SE zh-CN zh-TW; do
        [ "$_match" = "$locale" ] && _matched=1
      done
      [ $_matched -eq 1 ] && _l10ntarget=common || _l10ntarget=other
      echo %{_libdir}/xulrunner-%{version_internal}/extensions/langpack-$locale@firefox.mozilla.org \ \
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
rm -f $RPM_BUILD_ROOT%{_libdir}/pkgconfig/mozilla-plugin.pc
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
exit 0

%posttrans
# needed for updates which transition directory to symlink
%if 0%{?ga_version:1}
test -d %{_libdir}/xulrunner-%{ga_version} && rm -rf %{_libdir}/xulrunner-%{ga_version}
ln -sf xulrunner-%{version_internal} %{_libdir}/xulrunner-%{ga_version}
%endif
exit 0

%preun
if [ "$1" = "0" ]; then # deinstallation
  # that's not quite nice since old versions should be removed on update as well
  # but that's problematic for updates w/o raising the version number
  /usr/sbin/update-alternatives --remove xulrunner %{_libdir}/xulrunner-%{apiversion}/xulrunner
fi
exit 0

%files
%defattr(-,root,root)
%dir %{_libdir}/xulrunner-%{version_internal}/
%dir %{_libdir}/xulrunner-%{version_internal}/chrome/
%dir %{_libdir}/xulrunner-%{version_internal}/dictionaries/
%dir %{_libdir}/xulrunner-%{version_internal}/extensions/
%{_libdir}/xulrunner-%{version_internal}/chrome/icons/
%{_libdir}/xulrunner-%{version_internal}/components/
%{_libdir}/xulrunner-%{version_internal}/*.so
%if 0%{?shared_js} == 1
%exclude %{_libdir}/xulrunner-%{version_internal}/libmozjs.so
%endif
%{_libdir}/xulrunner-%{version_internal}/chrome.manifest
%{_libdir}/xulrunner-%{version_internal}/dependentlibs.list
%{_libdir}/xulrunner-%{version_internal}/mozilla-xremote-client
%{_libdir}/xulrunner-%{version_internal}/plugin-container
%{_libdir}/xulrunner-%{version_internal}/xulrunner
%{_libdir}/xulrunner-%{version_internal}/xulrunner-stub
%{_libdir}/xulrunner-%{version_internal}/platform.ini
%{_libdir}/xulrunner-%{version_internal}/omni.ja
%{_libdir}/xulrunner-%{version_internal}/README.xulrunner
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
# API symlink (already in mozilla-js)
%if 0%{?shared_js} == 0
%{_libdir}/xulrunner-%{apiversion}
%endif
# compat symlinks
%if 0%{?ga_version:1}
%ghost %{_libdir}/xulrunner-%{ga_version}
%endif

%if 0%{?shared_js} == 1
%files -n mozilla-js
%defattr(-,root,root)
%dir %{_libdir}/xulrunner-%{version_internal}/
%{_libdir}/xulrunner-%{apiversion}
%{_libdir}/xulrunner-%{version_internal}/libmozjs.so
%endif

%files devel
%defattr(-,root,root)
%{_libdir}/xulrunner-devel-%{version_internal}/
%{_libdir}/xulrunner-%{version_internal}/js-gdb.py
# FIXME symlink dynamic libs below sdk/lib
%attr(644,root,root) %{_libdir}/pkgconfig/*
%{_includedir}/xulrunner-%{version_internal}/
%{_datadir}/xulrunner-%{version_internal}/

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
