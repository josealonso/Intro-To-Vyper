import brownie
import pytest


INIT_NAME = "SampleToken"
INIT_SYMBOL = "ST"
INIT_DECIMALS = 18
INIT_SUPPLY = 1000


@pytest.fixture
def sampletoken_contract(SampleToken, accounts):
    yield SampleToken.deploy(INIT_NAME, INIT_SYMBOL, INIT_DECIMALS, INIT_SUPPLY, {'from': accounts[0]})


def test_initial_state(sampletoken_contract):
    assert sampletoken_contract.name() == INIT_NAME
    assert sampletoken_contract.symbol() == INIT_SYMBOL
    assert sampletoken_contract.decimals() == INIT_DECIMALS
    assert sampletoken_contract.totalSupply() == INIT_SUPPLY * 10 ** INIT_DECIMALS


def test_transfer(sampletoken_contract, accounts):
    values = 1000
    sampletoken_contract.transfer(accounts[1], values, {'from': accounts[0]})

    assert sampletoken_contract.balanceOf(accounts[1]) == values


def test_transferFrom(sampletoken_contract, accounts):
    values1 = 1000
    sampletoken_contract.transfer(accounts[1], values1, {'from': accounts[0]})

    values2 = 500
    sampletoken_contract.approve(accounts[0], values2, {'from': accounts[1]})
    sampletoken_contract.transferFrom(accounts[1], accounts[2], values2, {'from': accounts[0]})

    assert sampletoken_contract.balanceOf(accounts[2]) == values2


def test_mint(sampletoken_contract, accounts):
    with brownie.reverts():
        sampletoken_contract.mint(accounts[2], 1000, {'from': accounts[1]})

    sampletoken_contract.mint(accounts[1], 1000, {'from': accounts[0]})
    assert sampletoken_contract.balanceOf(accounts[1]) == 1000


def test_burn(sampletoken_contract, accounts):
    burned_value = 1000
    sampletoken_contract.burn(burned_value, {'from': accounts[0]})

    assert sampletoken_contract.totalSupply() < INIT_SUPPLY * 10 ** INIT_DECIMALS


def test_burnFrom(sampletoken_contract, accounts):
    sampletoken_contract.transfer(accounts[1], 1000, {'from': accounts[0]})

    burned_value = 500
    sampletoken_contract.approve(accounts[0], burned_value, {'from': accounts[1]})
    sampletoken_contract.burnFrom(accounts[1], burned_value, {'from': accounts[0]})
