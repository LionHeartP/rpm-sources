for FILE in ./configs/*.config; do
cat <<EOF >> $FILE
## for OpenRGB
CONFIG_I2C_NCT6775=m
## for tkg
CONFIG_ZENIFY=y
CONFIG_WINESYNC=y
CONFIG_USER_NS_UNPRIVILEGED=y
CONFIG_TCP_CONG_BBR2=m
# CONFIG_HZ_750 is not set
## for BBR2
CONFIG_DEFAULT_BBR2=n
## for cjktty since 6.3.5
CONFIG_FONT_CJK_16x16=y
CONFIG_FONT_CJK_32x32=y
## for bcachefs since 6.4.13
# CONFIG_MEM_ALLOC_PROFILING is not set
# CONFIG_CODETAG_FAULT_INJECTION is not set
## for march
# CONFIG_MK8SSE3 is not set
# CONFIG_MK10 is not set
# CONFIG_MBARCELONA is not set
# CONFIG_MBOBCAT is not set
# CONFIG_MJAGUAR is not set
# CONFIG_MBULLDOZER is not set
# CONFIG_MPILEDRIVER is not set
# CONFIG_MSTEAMROLLER is not set
# CONFIG_MEXCAVATOR is not set
# CONFIG_MZEN is not set
# CONFIG_MZEN2 is not set
# CONFIG_MZEN3 is not set
# CONFIG_MZEN4 is not set
# CONFIG_MNEHALEM is not set
# CONFIG_MWESTMERE is not set
# CONFIG_MSILVERMONT is not set
# CONFIG_MGOLDMONT is not set
# CONFIG_MGOLDMONTPLUS is not set
# CONFIG_MSANDYBRIDGE is not set
# CONFIG_MIVYBRIDGE is not set
# CONFIG_MHASWELL is not set
# CONFIG_MBROADWELL is not set
# CONFIG_MSKYLAKE is not set
# CONFIG_MSKYLAKEX is not set
# CONFIG_MCANNONLAKE is not set
# CONFIG_MICELAKE is not set
# CONFIG_MCASCADELAKE is not set
# CONFIG_MCOOPERLAKE is not set
# CONFIG_MTIGERLAKE is not set
# CONFIG_MSAPPHIRERAPIDS is not set
# CONFIG_MROCKETLAKE is not set
# CONFIG_MALDERLAKE is not set
# CONFIG_MNATIVE_INTEL is not set
# CONFIG_MNATIVE_AMD is not set
# CONFIG_GENERIC_CPU2 is not set
# CONFIG_GENERIC_CPU3 is not set
# CONFIG_GENERIC_CPU4 is not set
# CONFIG_MRAPTORLAKE is not set
# CONFIG_MMETEORLAKE is not set
# CONFIG_MEMERALDRAPIDS is not set
## device specific config
## Steam Deck
CONFIG_MFD_STEAMDECK=m
CONFIG_SENSORS_STEAMDECK=m
CONFIG_LEDS_STEAMDECK=m
CONFIG_EXTCON_STEAMDECK=m
CONFIG_DRM_AMD_COLOR_STEAMDECK=y
CONFIG_USB_DWC3_DUAL_ROLE=y
CONFIG_USB_DWC2_DUAL_ROLE=y
CONFIG_USB_DWC2_PCI=m
# CONFIG_USB_DWC2_DEBUG is not set
# CONFIG_USB_DWC2_TRACK_MISSED_SOFS is not set
CONFIG_USB_CHIPIDEA_UDC=y
CONFIG_USB_CHIPIDEA_HOST=y
CONFIG_USB_ISP1760_HCD=y
CONFIG_USB_ISP1761_UDC=y
CONFIG_USB_GADGET_VBUS_DRAW=2
CONFIG_USB_GADGET_STORAGE_NUM_BUFFERS=2
# CONFIG_USB_GADGET_DEBUG is not set
# CONFIG_USB_GADGET_DEBUG_FILES is not set
# CONFIG_USB_GADGET_DEBUG_FS is not set
# CONFIG_U_SERIAL_CONSOLE is not set
# CONFIG_USB_R8A66597 is not set
# CONFIG_USB_PXA27X is not set
# CONFIG_USB_MV_UDC is not set
# CONFIG_USB_MV_U3D is not set
# CONFIG_USB_M66592 is not set
# CONFIG_USB_BDC_UDC is not set
# CONFIG_USB_AMD5536UDC is not set
# CONFIG_USB_NET2272 is not set
# CONFIG_USB_NET2280 is not set
# CONFIG_USB_GOKU is not set
# CONFIG_USB_EG20T is not set
# CONFIG_USB_DUMMY_HCD is not set
# CONFIG_USB_CONFIGFS is not set
# CONFIG_PHY_SAMSUNG_USB2 is not set
## Microsoft Surface
CONFIG_HID_IPTS=m
CONFIG_HID_ITHC=m
CONFIG_SURFACE_BOOK1_DGPU_SWITCH=m
CONFIG_IPC_CLASSES=y
CONFIG_LEDS_TPS68470=m
CONFIG_SENSORS_SURFACE_FAN=m
CONFIG_SENSORS_SURFACE_TEMP=m
## Lenovo Legion
CONFIG_LEGION_LAPTOP=m
CONFIG_ACPI_CALL=m
CONFIG_SND_SOC_SOF=m
CONFIG_SND_SOC_SOF_PROBE_WORK_QUEUE=y
CONFIG_SND_SOC_SOF_IPC3=y
CONFIG_SND_SOC_SOF_INTEL_IPC4=y
CONFIG_SND_SOC_SOF_AMD_COMMON=m
CONFIG_SND_SOC_TOPOLOGY=y
## handheld shit
CONFIG_BMI323=m
CONFIG_IIO_HRTIMER_TRIGGER=m
CONFIG_IIO_SYSFS_TRIGGER=m
CONFIG_BMI160=m
CONFIG_BMI260_I2C=m
## t2 macbooks
CONFIG_DRM_APPLETBDRM=m
CONFIG_HID_APPLETB_BL=m
CONFIG_HID_APPLETB_KBD=m
CONFIG_HID_APPLE_MAGIC_BACKLIGHT=m
CONFIG_APPLE_BCE=m
## Wine NTSync
CONFIG_NTSYNC=y
## CachyOS BORE
CONFIG_SCHED_BORE=y

EOF
done

