// Fill out your copyright notice in the Description page of Project Settings.

#include "IntSpinBox.h"

UIntSpinBox::UIntSpinBox():
	USpinBox(), IntegerValue(GetIntFromFloat(Value)), DisplayValue(FText::AsNumber(IntegerValue)) {}

TSharedRef<SWidget> UIntSpinBox::RebuildWidget()
{
	MySpinBox = SNew(SSpinBox<float>)
		.Style(&WidgetStyle)
		.Font(Font)
		.ClearKeyboardFocusOnCommit(ClearKeyboardFocusOnCommit)
		.SelectAllTextOnCommit(SelectAllTextOnCommit)
		.OnValueChanged(BIND_UOBJECT_DELEGATE(FOnFloatValueChanged, MyHandleOnValueChanged))
		.OnValueCommitted(BIND_UOBJECT_DELEGATE(FOnFloatValueCommitted, HandleOnValueCommitted))
		.OnBeginSliderMovement(BIND_UOBJECT_DELEGATE(FSimpleDelegate, HandleOnBeginSliderMovement))
		.OnEndSliderMovement(BIND_UOBJECT_DELEGATE(FOnFloatValueChanged, HandleOnEndSliderMovement));
	return BuildDesignTimeWidget(MySpinBox.ToSharedRef());
}

void UIntSpinBox::MyHandleOnValueChanged(float InValue) {
	if (ValiddateIntegerValue(InValue)) {
		HandleOnValueChanged(InValue);
	}
}

bool UIntSpinBox::ValiddateIntegerValue(float& InValue) {
	if (Value != InValue) {
		InValue = Value < InValue ? FMath::CeilToFloat(InValue) : FMath::FloorToFloat(InValue);

		SetValue(InValue);

		IntegerValue = GetIntFromFloat(InValue);

		UpdateDisplayValue();
		return true;
	}
	return false;
}

int32 UIntSpinBox::GetIntFromFloat(const float& FloatValue) {
	if (FloatValue >= 0.0f) {
		return (int)(FloatValue + 0.5f);
	}
	return (int)(FloatValue - 0.5f);
}

void UIntSpinBox::UpdateDisplayValue() {
	DisplayValue = FText::AsNumber(IntegerValue);

}