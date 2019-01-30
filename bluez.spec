#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bluez
Version  : 5.50
Release  : 22
URL      : http://www.kernel.org/pub/linux/bluetooth/bluez-5.50.tar.xz
Source0  : http://www.kernel.org/pub/linux/bluetooth/bluez-5.50.tar.xz
Summary  : Bluetooth protocol stack for Linux
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: bluez-bin = %{version}-%{release}
Requires: bluez-config = %{version}-%{release}
Requires: bluez-data = %{version}-%{release}
Requires: bluez-lib = %{version}-%{release}
Requires: bluez-libexec = %{version}-%{release}
Requires: bluez-license = %{version}-%{release}
Requires: bluez-man = %{version}-%{release}
Requires: bluez-services = %{version}-%{release}
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libical)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(sbc)
BuildRequires : pkgconfig(speexdsp)
BuildRequires : readline-dev
BuildRequires : systemd-dev
Patch1: CVE-2018-10910.patch

%description
BlueZ - Bluetooth protocol stack for Linux
******************************************

%package bin
Summary: bin components for the bluez package.
Group: Binaries
Requires: bluez-data = %{version}-%{release}
Requires: bluez-libexec = %{version}-%{release}
Requires: bluez-config = %{version}-%{release}
Requires: bluez-license = %{version}-%{release}
Requires: bluez-man = %{version}-%{release}
Requires: bluez-services = %{version}-%{release}

%description bin
bin components for the bluez package.


%package config
Summary: config components for the bluez package.
Group: Default

%description config
config components for the bluez package.


%package data
Summary: data components for the bluez package.
Group: Data

%description data
data components for the bluez package.


%package dev
Summary: dev components for the bluez package.
Group: Development
Requires: bluez-lib = %{version}-%{release}
Requires: bluez-bin = %{version}-%{release}
Requires: bluez-data = %{version}-%{release}
Provides: bluez-devel = %{version}-%{release}

%description dev
dev components for the bluez package.


%package extras
Summary: extras components for the bluez package.
Group: Default

%description extras
extras components for the bluez package.


%package lib
Summary: lib components for the bluez package.
Group: Libraries
Requires: bluez-data = %{version}-%{release}
Requires: bluez-libexec = %{version}-%{release}
Requires: bluez-license = %{version}-%{release}

%description lib
lib components for the bluez package.


%package libexec
Summary: libexec components for the bluez package.
Group: Default
Requires: bluez-config = %{version}-%{release}
Requires: bluez-license = %{version}-%{release}

%description libexec
libexec components for the bluez package.


%package license
Summary: license components for the bluez package.
Group: Default

%description license
license components for the bluez package.


%package man
Summary: man components for the bluez package.
Group: Default

%description man
man components for the bluez package.


%package services
Summary: services components for the bluez package.
Group: Systemd services

%description services
services components for the bluez package.


%prep
%setup -q -n bluez-5.50
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548811812
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --enable-library \
--enable-manpages \
--with-dbusconfdir=/usr/share \
--enable-experimental \
--enable-deprecated
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1548811812
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bluez
cp COPYING %{buildroot}/usr/share/package-licenses/bluez/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/bluez/COPYING.LIB
%make_install
## install_append content
ln -sv bluetooth.service %{buildroot}/usr/lib/systemd/system/dbus-org.bluez.service
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/udev/hid2hci
/usr/lib64/cups/backend/bluetooth

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/ciptool
%exclude /usr/bin/hciattach
%exclude /usr/bin/hciconfig
%exclude /usr/bin/hcidump
%exclude /usr/bin/hcitool
%exclude /usr/bin/rfcomm
%exclude /usr/bin/sdptool
/usr/bin/bccmd
/usr/bin/bluemoon
/usr/bin/bluetoothctl
/usr/bin/btattach
/usr/bin/btmon
/usr/bin/hex2hcd
/usr/bin/l2ping
/usr/bin/l2test
/usr/bin/mpris-proxy
/usr/bin/rctest

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/97-hid2hci.rules

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/org.bluez.obex.service
/usr/share/dbus-1/system-services/org.bluez.service
/usr/share/dbus-1/system.d/bluetooth.conf

%files dev
%defattr(-,root,root,-)
/usr/include/bluetooth/bluetooth.h
/usr/include/bluetooth/bnep.h
/usr/include/bluetooth/cmtp.h
/usr/include/bluetooth/hci.h
/usr/include/bluetooth/hci_lib.h
/usr/include/bluetooth/hidp.h
/usr/include/bluetooth/l2cap.h
/usr/include/bluetooth/rfcomm.h
/usr/include/bluetooth/sco.h
/usr/include/bluetooth/sdp.h
/usr/include/bluetooth/sdp_lib.h
/usr/lib64/libbluetooth.so
/usr/lib64/pkgconfig/bluez.pc

%files extras
%defattr(-,root,root,-)
/usr/bin/ciptool
/usr/bin/hciattach
/usr/bin/hciconfig
/usr/bin/hcidump
/usr/bin/hcitool
/usr/bin/rfcomm
/usr/bin/sdptool
/usr/share/man/man1/ciptool.1
/usr/share/man/man1/hciattach.1
/usr/share/man/man1/hciconfig.1
/usr/share/man/man1/hcidump.1
/usr/share/man/man1/hcitool.1
/usr/share/man/man1/rfcomm.1
/usr/share/man/man1/sdptool.1

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbluetooth.so.3
/usr/lib64/libbluetooth.so.3.18.16

%files libexec
%defattr(-,root,root,-)
/usr/libexec/bluetooth/bluetoothd
/usr/libexec/bluetooth/obexd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bluez/COPYING
/usr/share/package-licenses/bluez/COPYING.LIB

%files man
%defattr(0644,root,root,0755)
%exclude /usr/share/man/man1/ciptool.1
%exclude /usr/share/man/man1/hciattach.1
%exclude /usr/share/man/man1/hciconfig.1
%exclude /usr/share/man/man1/hcidump.1
%exclude /usr/share/man/man1/hcitool.1
%exclude /usr/share/man/man1/rfcomm.1
%exclude /usr/share/man/man1/sdptool.1
/usr/share/man/man1/bccmd.1
/usr/share/man/man1/btattach.1
/usr/share/man/man1/hid2hci.1
/usr/share/man/man1/l2ping.1
/usr/share/man/man1/rctest.1
/usr/share/man/man8/bluetoothd.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/bluetooth.service
/usr/lib/systemd/system/dbus-org.bluez.service
/usr/lib/systemd/user/obex.service
