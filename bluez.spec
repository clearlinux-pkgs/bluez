#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bluez
Version  : 5.46
Release  : 10
URL      : http://www.kernel.org/pub/linux/bluetooth/bluez-5.46.tar.xz
Source0  : http://www.kernel.org/pub/linux/bluetooth/bluez-5.46.tar.xz
Summary  : Bluetooth protocol stack for Linux
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: bluez-bin
Requires: bluez-config
Requires: bluez-lib
Requires: bluez-data
Requires: bluez-doc
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(libical)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(sbc)
BuildRequires : pkgconfig(speexdsp)
BuildRequires : readline-dev
BuildRequires : systemd-dev
Patch1: bluez.patch

%description
BlueZ - Bluetooth protocol stack for Linux
******************************************

%package bin
Summary: bin components for the bluez package.
Group: Binaries
Requires: bluez-data
Requires: bluez-config

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
Requires: bluez-lib
Requires: bluez-bin
Requires: bluez-data
Provides: bluez-devel

%description dev
dev components for the bluez package.


%package doc
Summary: doc components for the bluez package.
Group: Documentation

%description doc
doc components for the bluez package.


%package lib
Summary: lib components for the bluez package.
Group: Libraries
Requires: bluez-data
Requires: bluez-config

%description lib
lib components for the bluez package.


%prep
%setup -q -n bluez-5.46
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505312526
%configure --disable-static --enable-library \
--enable-manpages \
--with-dbusconfdir=/usr/share
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1505312526
rm -rf %{buildroot}
%make_install
## make_install_append content
ln -sv bluetooth.service %{buildroot}/usr/lib/systemd/system/dbus-org.bluez.service
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib/udev/hid2hci
/usr/lib64/cups/backend/bluetooth

%files bin
%defattr(-,root,root,-)
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
/usr/libexec/bluetooth/bluetoothd
/usr/libexec/bluetooth/obexd

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/bluetooth.service
/usr/lib/systemd/system/dbus-org.bluez.service
/usr/lib/systemd/user/obex.service
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbluetooth.so.3
/usr/lib64/libbluetooth.so.3.18.15
